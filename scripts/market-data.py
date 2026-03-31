#!/usr/bin/env python3
"""
Hive Mind — Comprehensive Market Data Pull
Pulls prices for all crisis-relevant assets, computes deltas, flags significant moves.

Usage:
  python3 scripts/market-data.py              # Full report
  python3 scripts/market-data.py --json       # Output as JSON (for graph updates)
  python3 scripts/market-data.py --alerts     # Only show significant moves (>2% daily)

Data NOT available via yfinance (must be web-searched):
  - European TTF gas price
  - VLCC tanker day rates
  - Urea/DAP fertilizer prices
  - Helium spot prices (no public ticker — track via news)
  - Container shipping rates (use Freightos Baltic Index news)
  - War risk insurance premiums
  - Methanol spot price (Gulf/US)
  - Ammonia spot price
  - FAO Food Price Index (monthly)
  - India 10Y government bond yield
"""

import yfinance as yf
import json
import sys
from datetime import datetime, timedelta

# ============================================================
# FULL ASSET UNIVERSE — grouped by category
# ============================================================
ASSETS = {
    # --- ENERGY (direct crisis exposure) ---
    "Brent Crude": {"ticker": "BZ=F", "category": "energy", "unit": "$/bbl"},
    "WTI Crude": {"ticker": "CL=F", "category": "energy", "unit": "$/bbl"},
    "Natural Gas (Henry Hub)": {"ticker": "NG=F", "category": "energy", "unit": "$/MMBtu"},
    "Heating Oil": {"ticker": "HO=F", "category": "energy", "unit": "$/gal"},
    "RBOB Gasoline": {"ticker": "RB=F", "category": "energy", "unit": "$/gal"},

    # --- METALS (safe haven + industrial) ---
    "Gold": {"ticker": "GC=F", "category": "metals", "unit": "$/oz"},
    "Silver": {"ticker": "SI=F", "category": "metals", "unit": "$/oz"},
    "Copper": {"ticker": "HG=F", "category": "metals", "unit": "$/lb"},
    "Platinum": {"ticker": "PL=F", "category": "metals", "unit": "$/oz"},
    "Palladium": {"ticker": "PA=F", "category": "metals", "unit": "$/oz"},
    "Aluminum (LME)": {"ticker": "ALI=F", "category": "metals", "unit": "$/mt"},

    # --- AGRICULTURE / FOOD (food security, fertilizer downstream) ---
    "Wheat": {"ticker": "ZW=F", "category": "agriculture", "unit": "¢/bu"},
    "Corn": {"ticker": "ZC=F", "category": "agriculture", "unit": "¢/bu"},
    "Soybeans": {"ticker": "ZS=F", "category": "agriculture", "unit": "¢/bu"},
    "Rough Rice": {"ticker": "ZR=F", "category": "agriculture", "unit": "¢/cwt"},
    "Palm Oil (Malaysia)": {"ticker": "ZL=F", "category": "agriculture", "unit": "¢/lb"},  # Soybean oil as proxy; Malaysia palm oil web-search
    "Sugar": {"ticker": "SB=F", "category": "agriculture", "unit": "¢/lb"},

    # --- EQUITY INDICES (global coverage) ---
    # US
    "S&P 500": {"ticker": "^GSPC", "category": "equity_index", "unit": ""},
    "NASDAQ Composite": {"ticker": "^IXIC", "category": "equity_index", "unit": ""},
    "Dow Jones": {"ticker": "^DJI", "category": "equity_index", "unit": ""},
    # India
    "Nifty 50": {"ticker": "^NSEI", "category": "equity_index", "unit": ""},
    "Sensex": {"ticker": "^BSESN", "category": "equity_index", "unit": ""},
    "Bank Nifty": {"ticker": "^NSEBANK", "category": "equity_index", "unit": ""},
    # Gulf
    "Saudi Tadawul (TASI)": {"ticker": "^TASI.SR", "category": "equity_index", "unit": ""},
    # Europe
    "FTSE 100": {"ticker": "^FTSE", "category": "equity_index", "unit": ""},
    "DAX": {"ticker": "^GDAXI", "category": "equity_index", "unit": ""},
    "CAC 40 (France)": {"ticker": "^FCHI", "category": "equity_index", "unit": ""},
    "STOXX 600 (Europe)": {"ticker": "^STOXX", "category": "equity_index", "unit": ""},
    # Asia
    "Nikkei 225": {"ticker": "^N225", "category": "equity_index", "unit": ""},
    "Shanghai Composite": {"ticker": "000001.SS", "category": "equity_index", "unit": ""},
    "Hang Seng (HK)": {"ticker": "^HSI", "category": "equity_index", "unit": ""},
    "KOSPI (S. Korea)": {"ticker": "^KS11", "category": "equity_index", "unit": ""},
    "Taiwan TAIEX": {"ticker": "^TWII", "category": "equity_index", "unit": ""},
    "ASX 200 (Australia)": {"ticker": "^AXJO", "category": "equity_index", "unit": ""},
    # Latin America & EM
    "Bovespa (Brazil)": {"ticker": "^BVSP", "category": "equity_index", "unit": ""},
    "MSCI EM ETF (EEM)": {"ticker": "EEM", "category": "equity_index", "unit": "$"},

    # --- SECTOR ETFs (who's winning/losing from the war) ---
    "Energy Sector (XLE)": {"ticker": "XLE", "category": "sector_etf", "unit": "$"},
    "Defense & Aero (ITA)": {"ticker": "ITA", "category": "sector_etf", "unit": "$"},
    "Semiconductors (SMH)": {"ticker": "SMH", "category": "sector_etf", "unit": "$"},
    "Shipping (BOAT)": {"ticker": "BOAT", "category": "sector_etf", "unit": "$"},
    "Uranium (URA)": {"ticker": "URA", "category": "sector_etf", "unit": "$"},

    # --- KEY SINGLE STOCKS (crisis bellwethers) ---
    "Exxon Mobil": {"ticker": "XOM", "category": "stock", "unit": "$"},
    "Lockheed Martin": {"ticker": "LMT", "category": "stock", "unit": "$"},
    "Cheniere Energy (LNG)": {"ticker": "LNG", "category": "stock", "unit": "$"},
    "Frontline (Tankers)": {"ticker": "FRO", "category": "stock", "unit": "$"},
    "CF Industries": {"ticker": "CF", "category": "stock", "unit": "$"},
    "Nutrien": {"ticker": "NTR", "category": "stock", "unit": "$"},
    "Linde": {"ticker": "LIN", "category": "stock", "unit": "$"},
    "BASF": {"ticker": "BAS.DE", "category": "stock", "unit": "€"},

    # --- BONDS & YIELDS ---
    "US 10Y Yield": {"ticker": "^TNX", "category": "bond", "unit": "%"},
    "US 2Y Yield": {"ticker": "^IRX", "category": "bond", "unit": "%"},
    "VIX (Fear Index)": {"ticker": "^VIX", "category": "bond", "unit": ""},

    # --- CURRENCIES (dollar strength, EM stress, commodity currencies) ---
    "USD/INR": {"ticker": "INR=X", "category": "currency", "unit": "₹"},
    "DXY (Dollar Index)": {"ticker": "DX-Y.NYB", "category": "currency", "unit": ""},
    "EUR/USD": {"ticker": "EURUSD=X", "category": "currency", "unit": ""},
    "USD/CNY": {"ticker": "CNY=X", "category": "currency", "unit": ""},
    "GBP/USD": {"ticker": "GBPUSD=X", "category": "currency", "unit": ""},
    "USD/JPY": {"ticker": "JPY=X", "category": "currency", "unit": "¥"},
    "AUD/USD": {"ticker": "AUDUSD=X", "category": "currency", "unit": ""},
    "USD/BRL": {"ticker": "BRL=X", "category": "currency", "unit": "R$"},
    "USD/TRY": {"ticker": "TRY=X", "category": "currency", "unit": "₺"},
    "USD/KRW": {"ticker": "KRW=X", "category": "currency", "unit": "₩"},
}

# Significant move thresholds
ALERT_THRESHOLD_1D = 2.0    # Flag if >2% daily move
ALERT_THRESHOLD_1M = 10.0   # Flag if >10% monthly move

def fetch_data(name, info):
    """Fetch price data for a single asset."""
    try:
        t = yf.Ticker(info["ticker"])
        hist = t.history(period="3mo")
        if hist.empty or len(hist) < 2:
            return None

        current = float(hist['Close'].iloc[-1])
        prev = float(hist['Close'].iloc[-2])
        d1 = (current - prev) / prev * 100

        # 1 month ago (~22 trading days)
        idx_1m = max(0, len(hist) - 22)
        m1_price = float(hist['Close'].iloc[idx_1m])
        d1m = (current - m1_price) / m1_price * 100

        # 3 month (first available)
        m3_price = float(hist['Close'].iloc[0])
        d3m = (current - m3_price) / m3_price * 100

        is_alert = abs(d1) >= ALERT_THRESHOLD_1D or abs(d1m) >= ALERT_THRESHOLD_1M

        return {
            "name": name,
            "ticker": info["ticker"],
            "category": info["category"],
            "unit": info["unit"],
            "price": current,
            "delta_1d": d1,
            "delta_1m": d1m,
            "delta_3m": d3m,
            "date": hist.index[-1].strftime('%Y-%m-%d'),
            "alert": is_alert
        }
    except Exception as e:
        return {"name": name, "ticker": info["ticker"], "error": str(e)}


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--full"
    results = []
    errors = []

    print(f"Fetching {len(ASSETS)} assets...", file=sys.stderr)

    for name, info in ASSETS.items():
        r = fetch_data(name, info)
        if r is None:
            errors.append(name)
        elif "error" in r:
            errors.append(f"{name}: {r['error']}")
        else:
            results.append(r)

    if mode == "--json":
        print(json.dumps(results, indent=2))
        return

    # Group by category
    categories = {}
    for r in results:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)

    cat_labels = {
        "energy": "ENERGY",
        "metals": "METALS",
        "agriculture": "AGRICULTURE / FOOD",
        "equity_index": "EQUITY INDICES",
        "sector_etf": "SECTOR ETFs",
        "stock": "BELLWETHER STOCKS",
        "bond": "BONDS & VOLATILITY",
        "currency": "CURRENCIES"
    }

    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(f"\n{'='*80}")
    print(f"  HIVE MIND MARKET DATA — {now}")
    print(f"  {len(results)} assets fetched | Alerts flagged at >{ALERT_THRESHOLD_1D}% daily or >{ALERT_THRESHOLD_1M}% monthly")
    print(f"{'='*80}\n")

    alerts = [r for r in results if r.get("alert")]
    if alerts:
        print(f"  *** {len(alerts)} SIGNIFICANT MOVES ***")
        for r in sorted(alerts, key=lambda x: abs(x["delta_1d"]), reverse=True):
            flag = "▲" if r["delta_1d"] > 0 else "▼"
            print(f"  {flag} {r['name']:30s} {r['unit']}{r['price']:>10.2f}  1D: {r['delta_1d']:>+6.1f}%  1M: {r['delta_1m']:>+6.1f}%")
        print()

    if mode == "--alerts":
        if not alerts:
            print("  No significant moves today.")
        return

    for cat_key in ["energy", "metals", "agriculture", "equity_index", "sector_etf", "stock", "bond", "currency"]:
        if cat_key not in categories:
            continue
        print(f"  {cat_labels.get(cat_key, cat_key)}")
        print(f"  {'─'*76}")
        for r in categories[cat_key]:
            flag = " *** " if r.get("alert") else "     "
            print(f"{flag}{r['name']:30s} {r['unit']}{r['price']:>10.2f}  │ 1D: {r['delta_1d']:>+6.1f}% │ 1M: {r['delta_1m']:>+6.1f}% │ 3M: {r['delta_3m']:>+6.1f}%")
        print()

    if errors:
        print(f"  FAILED ({len(errors)}): {', '.join(errors[:5])}")

    print(f"\n  NOTE: These assets require web search (not on yfinance):")
    print(f"  • European TTF natural gas price")
    print(f"  • VLCC tanker day rates (Clarksons/Baltic Exchange)")
    print(f"  • Urea / DAP fertilizer prices (Argus/CRU)")
    print(f"  • Helium spot price (no public ticker — news search)")
    print(f"  • Container freight rates (Freightos Baltic Index)")
    print(f"  • Marine war risk insurance premiums")
    print(f"  • India 10Y government bond yield (RBI data)")


if __name__ == "__main__":
    main()
