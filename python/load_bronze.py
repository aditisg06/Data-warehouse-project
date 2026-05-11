from procedures import run_stored_procedure

def load_bronze():

    run_stored_procedure(
        "bronze.load_bronze",
        "Bronze"
    )

if __name__ == "__main__":
    load_bronze()