from vanRental import VanRental, Customer



def main():

    shop = VanRental(50)

    customer = Customer()



    while True:

        print("""

        ====== Van Rental Shop =======

        1. Display available Vans
        
        2. Request a Van on hourly basis $15
            + 10 € booking charge
        
        3. Request a Van on daily basis $40
            + 10 € booking charge
        
        4. Request a Van on weekly basis $120
            + 10 € booking charge
        
        5. Return a Van
        
        6. Exit

        """)

        

        choice = input("Enter choice: ")

        

        try:

            choice = int(choice)

        except ValueError:

            print("That's not an int!")

            continue

        

        if choice == 1:

            shop.displaystock()

        

        elif choice == 2:

            customer.rentalTime = shop.rentVanOnHourlyBasis(customer.requestVan())

            customer.rentalBasis = 1
            #print( "xxx customer.rentalTime" , customer.rentalTime,"xxx"  )


        elif choice == 3:

            customer.rentalTime = shop.rentVanOnDailyBasis(customer.requestVan())

            customer.rentalBasis = 2



        elif choice == 4:

            customer.rentalTime = shop.rentVanOnWeeklyBasis(customer.requestVan())

            customer.rentalBasis = 3



        elif choice == 5:

            customer.bill = shop.returnVan(customer.returnVan())

            customer.rentalBasis, customer.rentalTime, customer.Vans = 0,0,0        

        elif choice == 6:

            break

        else:

            print("Invalid input. Please enter number between 1-6 ")        

    print("Thank you for using the Van rental system.")



    

if __name__=="__main__":

    main()
    