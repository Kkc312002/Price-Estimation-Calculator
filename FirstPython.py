def calculate_handmade_project():
    return 1000

def calculate_decorative_project(pages, decoration_type, content_by_customer, due_date, level):
    price = 1000
    if due_date == "Urgent":
        price += 500
    if content_by_customer == "No":
        price += 50 * pages
    if level == "College":
        price *= 2
    return price + 1000

def calculate_assignment_writing(pages, pictures, content_by_customer, due_date, level):
    price = 600
    if due_date == "Urgent":
        price += 500
    if pictures == "Yes":
        picture_count = int(input("Enter the number of pictures: "))
        price += 100 * picture_count
    if content_by_customer == "No":
        price += 50 * pages
    if level == "College":
        price *= 2
    return price + 1000

def calculate_paintings(sheet_size, quantity, quality_level, due_date, level):
    sheet_size_prices = {"A2": 800, "A3": 500, "A4": 200, "Other": 0}
    price = sheet_size_prices.get(sheet_size, 0) * quantity
    if due_date == "Urgent":
        price += 500
    if quality_level == "Decent":
        price += 500
    elif quality_level == "Heavy":
        price += 1000
    if level == "College":
        price *= 2
    return price + 1000

def calculate_charts_posters(sheet_size, quantity, pictures, content_by_customer, quality_level, due_date, level):
    sheet_size_prices = {"Full Size": 1000, "A2": 800, "A3": 500, "A4": 200, "Other": 0}
    price = sheet_size_prices.get(sheet_size, 0) * quantity
    if due_date == "Urgent":
        price += 500
    if pictures == "Yes":
        picture_count = int(input("Enter the number of pictures: "))
        price += 100 * picture_count
    if content_by_customer == "No":
        price += 50 * quantity
    if quality_level == "Decent":
        price += 500
    elif quality_level == "Heavy":
        price += 1000
    if level == "College":
        price *= 2
    return price + 1000

def calculate_3d_models_crafts(type, size, material_cost, effort_level, due_date, level):
    price = 1000
    if due_date == "Urgent":
        price += 500
    if level == "College":
        price *= 2
    return price + 1000

def main():
    print("Welcome to Handmade Project Price Estimator Calculator!")
    while True:
        print("\nSelect the type of project you want to estimate the price for:")
        print("1. Decorative Project\n2. Assignment Writing\n3. Paintings\n4. Charts/Posters\n5. 3D Models/Crafts")
        print("6. Stop program")
        project_type = input("Enter your choice (1-6): ")
        
        if project_type == "6":
            print("Exiting program...")
            break
        
        project_type = int(project_type)
        
        level = input("Is this a school level or college level project? (School/College): ")
        
        if project_type == 1:
            pages = int(input("Enter total number of pages: "))
            decoration_type = input("Enter decoration type (Decent/Heavy): ")
            content_by_customer = input("Is content provided by customer? (Yes/No): ")
            due_date = input("Is the due date urgent? (Urgent/Non Urgent): ")
            price = calculate_decorative_project(pages, decoration_type, content_by_customer, due_date, level)
        elif project_type == 2:
            pages = int(input("Enter total number of pages: "))
            pictures = input("Are pictures included? (Yes/No): ")
            content_by_customer = input("Is content provided by customer? (Yes/No): ")
            due_date = input("Is the due date urgent? (Urgent/Non Urgent): ")
            price = calculate_assignment_writing(pages, pictures, content_by_customer, due_date, level)
        elif project_type == 3:
            sheet_size = input("Enter sheet size (A2/A3/A4/Other): ")
            quantity = int(input("Enter quantity: "))
            quality_level = input("Enter quality level (Decent/Heavy): ")
            due_date = input("Is the due date urgent? (Urgent/Non Urgent): ")
            price = calculate_paintings(sheet_size, quantity, quality_level, due_date, level)
        elif project_type == 4:
            sheet_size = input("Enter sheet size (Full Size/A2/A3/A4/Other): ")
            quantity = int(input("Enter quantity: "))
            pictures = input("Are pictures included? (Yes/No): ")
            content_by_customer = input("Is content provided by customer? (Yes/No): ")
            quality_level = input("Enter quality level (Decent/Heavy): ")
            due_date = input("Is the due date urgent? (Urgent/Non Urgent): ")
            price = calculate_charts_posters(sheet_size, quantity, pictures, content_by_customer, quality_level, due_date, level)
        elif project_type == 5:
            type = input("Enter type (Working/Non-Working): ")
            size = input("Enter size (Standard/Custom): ")
            material_cost = input("Enter material cost (Low/Medium/High): ")
            effort_level = input("Enter effort level (Low/Medium/High): ")
            due_date = input("Is the due date urgent? (Urgent/Non Urgent): ")
            price = calculate_3d_models_crafts(type, size, material_cost, effort_level, due_date, level)
        else:
            print("Invalid choice!")
            continue
        
        print("Estimated price for the project: ₹", price)

if __name__ == "__main__":
    main()
