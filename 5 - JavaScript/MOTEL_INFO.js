// QAP4.js

/**
 * Represents a customer at a motel.
 * @constructor
 * @param {string} name             - The name of the customer.
 * @param {string} birthDate        - The birth date of the customer in 'YYYY-MM-DD' format.
 * @param {string} gender           - The gender of the customer.
 * @param {Array} roomPreferences   - An array of room preferences.
 * @param {string} paymentMethod    - The payment method of the customer.
 * @param {Object} mailingAddress   - An object containing the mailing address details of the customer.
 * @param {string} phoneNumber - The phone number of the customer.
 * @param {string} checkInDate - The check-in date of the customer in 'YYYY-MM-DD' format.
 * @param {string} checkOutDate - The check-out date of the customer in 'YYYY-MM-DD' format.
 */

function Customer(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
    this.name = name;                       // Name
    this.birthDate = new Date(birthDate);  // birthDate is a string in 'YYYY-MM-DD' format
    this.gender = gender;                   // Gender
    this.roomPreferences = roomPreferences;  // Array of preferences
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress;  // Object with address details
    this.phoneNumber = phoneNumber;
    this.checkInDate = new Date(checkInDate);  // checkInDate is a string in 'YYYY-MM-DD' format
    this.checkOutDate = new Date(checkOutDate);  // checkOutDate is a string in 'YYYY-MM-DD' format

    this.getAge = function() {
        const today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        const m = today.getMonth() - this.birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < this.birthDate.getDate())) {
            age--;
        }
        return age;
    };

    this.getDurationOfStay = function() {
        const diffTime = Math.abs(this.checkOutDate - this.checkInDate);
        return Math.ceil(diffTime / (1000 * 60 * 60 * 24));  // Convert to days
    };

    this.describe = function() {
        return `Customer Profile: ${this.name} is a ${this.getAge()}-year-old ${this.gender} who prefers ${this.roomPreferences.join(', ')} rooms. Contact details: ${this.phoneNumber}, ${Object.values(this.mailingAddress).join(', ')}. Stay Duration: ${this.getDurationOfStay()} day(s) with ${this.paymentMethod} as the payment method.`;
    };
}

// Example usage
let customer = new Customer(
    "Dave Husk",
    "1983-08-24",
    "male",
    ["non--cigarette-smoking", "ADHD enthusiast"],
    "credit card",
    { street: "123 Topsail Rd", city: "St John's", province: "NL", postal: "A1A1A1", country: "CA" },
    "709-631-7414",
    "2023-11-25",
    "2023-11-30"
);

console.log(customer.describe());
