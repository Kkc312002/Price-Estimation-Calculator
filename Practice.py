def calculate_price():
    while True:
        print("Choose the type of project:")
        print("1. Handmade Decorative Projects")
        print("2. Assignment Writing")
        print("3. Painting")
        print("4. Charts")
        print("5. 3D Models and Crafts")
        print("6. Academic Writing")
        print("7. Graphic Designing")
        print("8. Coding/Development Projects")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pages = int(input("Enter the number of pages (min 15): "))
            decoration = input("Is the decoration decent or heavy? (decent/heavy): ")
            if pages < 15:
                print("Minimum order must be of 15 pages.")
                continue
            if decoration == 'decent':
                price_per_page = 20
            elif decoration == 'heavy':
                price_per_page = 40
            else:
                print("Invalid decoration type.")
                continue
            total_price = pages * price_per_page
            print("Estimated cost: Rs.", total_price)

        elif choice == '2':
            pages = int(input("Enter the number of pages: "))
            picture = input("Are there pictures included? (yes/no): ")
            if picture == 'yes':
                print("Contact your manager for pricing including pictures.")
            elif picture == 'no':
                total_price = 8 * pages
                print("Estimated cost: Rs.", total_price)
            else:
                print("Invalid input.")
                continue

        elif choice == '3':
            size = input("Enter the size (a2/a3/a4): ")
            decoration = input("Is the decoration decent or heavy? (decent/heavy): ")
            if size == 'a2':
                if decoration == 'decent':
                    total_price = 400
                elif decoration == 'heavy':
                    total_price = 600
                else:
                    print("Invalid decoration type.")
                    continue
            elif size == 'a3':
                if decoration == 'decent':
                    total_price = 200
                elif decoration == 'heavy':
                    total_price = 500
                else:
                    print("Invalid decoration type.")
                    continue
            elif size == 'a4':
                if decoration == 'decent':
                    total_price = 400
                elif decoration == 'heavy':
                    total_price = 700
                else:
                    print("Invalid decoration type.")
                    continue
            else:
                print("Invalid size.")
                continue
            print("Estimated cost: Rs.", total_price)

        elif choice == '4':
            print("Full size chart would cost around Rs. 400 to Rs. 700.")

        elif choice == '5':
            size = input("Enter the size (standard): ")
            working = input("Is it working or non-working? (working/non working): ")
            if working == 'working':
                total_price = 2000
            elif working == 'non working':
                total_price = 800
            else:
                print("Talk to manager for pricing.")
                continue
            print("Estimated cost: Rs.", total_price)

        elif choice == '6':
            pages = int(input("Enter the number of pages (min 20, max 100): "))
            plag = input("Is plagiarism included? (yes/no): ")
            if pages < 20 or pages > 100:
                print("Number of pages must be between 20 and 100.")
                continue
            if plag == 'yes':
                total_price = 1000
            elif plag == 'no':
                total_price = 3000
            else:
                print("Invalid input.")
                continue
            print("Estimated cost: Rs.", total_price)

        elif choice == '7':
            effort = input("Enter the effort level (low/average/high): ")
            if effort == 'low':
                total_price = 100
            elif effort == 'average':
                total_price = 200
            elif effort == 'high':
                total_price = 400
            else:
                print("Invalid input.")
                continue
            print("Estimated cost: Rs.", total_price)

        elif choice == '8':
            project_type = input("Enter the project type (school/college/corporate): ")
            if project_type == 'school':
                total_price = 1000
            elif project_type == 'college':
                total_price = 2000
            elif project_type == 'corporate':
                total_price = 5000
            else:
                print("Consult your manager for pricing.")
                continue
            print("Estimated cost: Rs.", total_price)

        elif choice == '9':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    calculate_price()
