# BankAPI
* Place the creds.json(Google Api Json file ) file in project csv folder.
* Run requirement.txt file.

* To start the server use command 
    ```
      $ python3 manage.py runserver
    ```
* To test the all three mentioned api use file(Bank_API/test.py) and uncomment the method
  - Records that do not have"cellular" contact
   
    * Source(Google Sheet)
       ```
       $ getcontact("cellular")
       ```
    * Source(CSV file)
       ```
        $ getcontact("cellular",Sheet=False)
       ```
  - Use "day" and "month" column values and find recordswhich are after 15th October
    * Source(Google Sheet)
      ```
      $ getdates(15,"oct")
      ```
    * Source(CSV file)
      ```
      $ getdates(15,"oct",Sheet=False)
      ```
  - Records having a specific marital status and between certain age group
    * Source(Google Sheet)
       ```
       $ getMarital(20,50,"married")
       ```
    * Source(CSV file)
       ```
       $ getMarital(20,50,"married",Sheet=False)
       ```

