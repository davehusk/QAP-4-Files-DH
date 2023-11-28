class Entity:
    def __init__(self, name, attributes, relationships, file_name=None, defaults=None):
        self.name = name
        self.attributes = attributes
        self.relationships = relationships
        self.file_name = file_name
        self.defaults = defaults

    def display(self):
        print(f"Entity: {self.name}")
        if self.file_name:
            print(f"File Name: {self.file_name}")
        if self.defaults:
            print("Defaults: " + ", ".join([f"{key}: {value}" for key, value in self.defaults.items()]))
        print("Attributes: " + ", ".join(self.attributes))
        for rel in self.relationships:
            print(f"Relationship: {rel}")

def main():
    # Define entities and their attributes
    customer = Entity("Customer", 
                      ["CustomerID (PK)", "Name", "Address", "Phone", "CreditCardNumber", "CreditCardExpiry"],
                      ["RoomStatus", "Bookings", "Revenue"])

    room = Entity("Room", 
                  ["RoomNumber (PK)", "MaintenanceStatus"],
                  ["RoomStatus"])

    room_status = Entity("RoomStatus", 
                         ["RoomNumber (FK)", "CustomerID (FK)", "CheckInDate", "CheckOutDate", "EarlyCheckIn", "ExtraBed", "ExtraKey", "LateCheckOut"],
                         [],
                         "RoomStatus.dat",
                         {"Vacant": "Special case where Customer Name is 'Vacant' if room is empty"})

    bookings = Entity("Bookings", 
                      ["BookingID (PK)", "CustomerID (FK)", "CheckInDate", "CheckOutDate"],
                      [],
                      "Bookings.dat")

    revenue = Entity("Revenue", 
                     ["InvoiceNumber (PK)", "InvoiceDate", "CustomerID (FK)", "PaymentMethod", "RoomCharge", "ExtrasCharge", "Subtotal", "Taxes", "Total"],
                     [],
                     "Revenue.dat")

    supplies = Entity("Supplies", 
                      ["ItemID (PK)", "Description", "InventoryLevel", "ReorderLevel"],
                      [],
                      "Supplies.dat")

    defaults = Entity("Defaults",
                      ["InvoiceNumber", "RoomRate", "HSTRate", "EarlyCheckInRate", "ExtraBedRate", "ExtraKeyRate", "LateCheckOutRate"],
                      [],
                      "STDef.dat",
                      {"InvoiceNumber": "1856", "RoomRate": "$75.00", "HSTRate": "15%", "EarlyCheckInRate": "$12.00", "ExtraBedRate": "$7.00 per night", "ExtraKeyRate": "$2.00", "LateCheckOutRate": "$12.00"})

    # Display the ERD structure
    for entity in [customer, room, room_status, bookings, revenue, supplies, defaults]:
        entity.display()
        print("\n")

if __name__ == "__main__":
    main()
