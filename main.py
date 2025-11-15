from utils.data_handler import query_data

def main():
    print("⚡ Electricity Consumption Query Bot ⚡")
    print("Ask me anything about electricity usage (type 'exit' to quit)")
    print("------------------------------------------------------------")

    while True:
        query = input("\nQuery: ").strip()
        if query.lower() in ["exit", "quit", "q"]:
            print("\nExiting... Goodbye!")
            break

        try:
            response = query_data(query)
            print(response)
            print("------------------------------------------------------------")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("------------------------------------------------------------")

if __name__ == "__main__":
    main()
