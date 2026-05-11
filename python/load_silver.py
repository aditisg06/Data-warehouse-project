from procedures import run_stored_procedure

def load_silver():

    run_stored_procedure(
        "silver.load_silver",
        "Silver"
    )

if __name__ == "__main__":
    load_silver()