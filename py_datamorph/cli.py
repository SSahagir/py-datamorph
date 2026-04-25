import argparse
import sys
from .converter import DataMorphConverter
from .cleaner import DataMorphCleaner

def main():
    parser = argparse.ArgumentParser(
        description="🚀 py-datamorph: The All-in-One Data Engineering Toolkit",
        epilog="Developed by Sk Sahagir for advanced data manipulation."
    )
    
    # Feature Grouping
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--csv2json', metavar='FILE', help="Transform CSV to JSON")
    group.add_argument('--json2csv', metavar='FILE', help="Transform JSON to CSV")
    group.add_argument('--xml2json', metavar='FILE', help="Transform XML to JSON")
    group.add_argument('--clean', metavar='FILE', help="Deep clean and optimize CSV")
    group.add_argument('--stats', metavar='FILE', help="Generate dataset analysis report")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    conv = DataMorphConverter()
    clean = DataMorphCleaner()

    try:
        if args.csv2json:
            result = conv.csv_to_json(args.csv2json)
            print(f"✅ CONVERSION SUCCESS: {result}")
        elif args.json2csv:
            result = conv.json_to_csv(args.json2csv)
            print(f"✅ CONVERSION SUCCESS: {result}")
        elif args.xml2json:
            result = conv.xml_to_json(args.xml2json)
            print(f"✅ CONVERSION SUCCESS: {result}")
        elif args.clean:
            result = clean.deep_clean(args.clean)
            print(f"🧹 CLEANING COMPLETE: {result}")
        elif args.stats:
            stats = clean.get_stats(args.stats)
            print("\n" + "="*30 + "\n📊 DATASET STATISTICS\n" + "="*30)
            for key, value in stats.items():
                print(f"{key:<15}: {value}")
            print("="*30)
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()