import datetime



class VanRental:

    

    def __init__(self,stock=0):

        """

        Our constructor class that instantiates Van rental shop.

        """



        self.stock = stock



    def displaystock(self):

        """

        Displays the Vans currently available for rent in the shop.

        """



        print("We have currently {} Vans available to rent.".format(self.stock))

        return self.stock



    def rentVanOnHourlyBasis(self, n):

        """

        Rents a Van on hourly basis to a customer.

        """

        if n <= 0:

            print("Number of Vans should be positive!")

            return None

        

        elif n > self.stock:

            print("Sorry! We have currently {} Vans available to rent.".format(self.stock))

            return None

        

        else:

            now = datetime.datetime.now()                      

            print("You have rented a {} Van(s) on hourly basis today at {} hours.".format(n,now.hour))

            print("You will be charged $5 for each hour per Van.")

            print("We hope that you enjoy our service.")



            self.stock -= n

            return now      

     

    def rentVanOnDailyBasis(self, n):

        """

        Rents a Van on daily basis to a customer.

        """

        if n <= 0:

            print("Number of Vans should be positive!")

            return None



        elif n > self.stock:

            print("Sorry! We have currently {} Vans available to rent.".format(self.stock))

            return None

    

        else:

            now = datetime.datetime.now()                      

            print("You have rented {} Van(s) on daily basis today at {} hours.".format(n, now.hour))

            print("You will be charged $20 for each day per Van.")

            print("We hope that you enjoy our service.")



            self.stock -= n

            return now

        

    def rentVanOnWeeklyBasis(self, n):

        """

        Rents a Van on weekly basis to a customer.

        """

        if n <= 0:

            print("Number of Vans should be positive!")

            return None



        elif n > self.stock:

            print("Sorry! We have currently {} Vans available to rent.".format(self.stock))

            return None        

        

        else:

            now = datetime.datetime.now()

            print("You have rented {} Van(s) on weekly basis today at {} hours.".format(n, now.hour))

            print("You will be charged $60 for each week per Van.")

            print("We hope that you enjoy our service.")

            self.stock -= n



            return now

    



    

    def returnVan(self, request):

        """

        1. Accept a rented Van from a customer

        2. Replensihes the inventory

        3. Return a bill

        """

        rentalTime, rentalBasis, numOfVans = request

        bill = 0



        if rentalTime and rentalBasis and numOfVans:

            self.stock += numOfVans

            now = datetime.datetime.now()

            rentalPeriod = now - rentalTime

        

            # hourly bill calculation

            if rentalBasis == 1:

                bill = 10 + round(rentalPeriod.seconds / 3600) * 15 * numOfVans

                

            # daily bill calculation

            elif rentalBasis == 2:

                bill = 10 + round(rentalPeriod.days) * 40 * numOfVans

                

            # weekly bill calculation

            elif rentalBasis == 3:

                bill = 10 + round(rentalPeriod.days / 7) * 120 * numOfVans

            

               

            if (3 <= numOfVans <= 50):

                print("You are eligible for special rental promotion of 30% discount")

                bill = bill * 0.7 



            print("Thanks for returning your Van. Hope you enjoyed our service!")

            print("That would be ${}".format(bill))

            return bill 

        else:

            print("Are you sure you rented a Van with us?")

            return None







class Customer:



    def __init__(self):

        """

        Our constructor method which instantiates various customer objects.

        """

        

        self.Vans = 0

        self.rentalBasis = 0

        self.rentalTime = 0

        self.bill = 0



    

    def requestVan(self):

        """

        Takes a request from the customer for the number of Vans.

        """

                      

        Vans = input("How many Vans would you like to rent?")

        try:

            Vans = int(Vans)

        except ValueError:

            print("That's not a positive integer!")

            return -1



        if Vans < 1:

            print("Invalid input. Number of Vans should be greater than zero!")

            return -1

        else:

            self.Vans = Vans

        return self.Vans

     

    def returnVan(self):

        """

        Allows customers to return their Vans to the rental shop.

        """

        if self.rentalBasis and self.rentalTime and self.Vans:

            return self.rentalTime, self.rentalBasis, self.Vans  

        else:

            return 0,0,0