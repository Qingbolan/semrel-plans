"""Import the supplied research project with per-record coverage receipts."""
import argparse
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
sys.path.insert(0,str(ROOT/'scripts/audit'))
from workload_import import WorkloadProjectImporter
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source',type=Path);args=parser.parse_args()
    print(WorkloadProjectImporter(ROOT,args.source).run())
