from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "US_flash_crash"
BBO_DIR = DATA_DIR / "bbo"
TRADE_DIR = DATA_DIR / "trade"

# We create a 'processed' folder in the root to store calculated features
PROCESSED_DIR = ROOT / "processed"
FEATURES_OUTPUT_DIR = PROCESSED_DIR / "features"

FEATURES_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BBO_FILE_PATTERN = "*.parquet" 
TRADE_FILE_PATTERN = "*.parquet"

if __name__ == "__main__":
    print(f"Project Root: {ROOT}")
    print(f"BBO Data: {BBO_DIR}")
    print(f"Trade Data: {TRADE_DIR}")
    
    if TRADE_DIR.exists():
        tickers = [p.name for p in TRADE_DIR.iterdir() if p.is_dir()]
        print(f"Found {len(tickers)} tickers. Example: {tickers[:5]}")