import importlib.metadata as metadata  # for version
import importlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def check_dependencies():
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    libraries = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    missing = False
    for lib, desc in libraries.items():
        try:
            # try to tmpport lib
            importlib.import_module(lib)
            # version of lib
            version = metadata.version(lib)
            print(f"[OK] {lib} ({version}) - {desc}")
        except ImportError:
            print(f"[ERROR] {lib} is missing!")
            missing = True

    if missing:
        print("\nError: Dependencies missing.")
        print("Install with: pip install -r requirements.txt\
            OR poetry install")
        return False
    return True


def run_analysis():
    #  NumPy
    print("\nAnalyzing Matrix data...")
    data = np.random.rand(1000, 3)
    print(f"Processing {len(data)} data points...")

    #   Pandas & Matplotlib
    print("Generating visualization...")
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    plt.figure()
    plt.scatter(df['A'], df['B'], c=df['C'], cmap='Greens')
    plt.savefig('matrix_analysis.png')
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_dependencies():
        run_analysis()
