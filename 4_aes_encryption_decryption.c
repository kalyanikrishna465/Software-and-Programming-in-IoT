#include <AES.h>

// Create an AES object
AES aes;

// Define your secret key (16 characters for AES-128)
const char* secretKey = "1234567890123456"; // 128-bit key
// Buffer to store the encrypted and decrypted data
char buffer[32]; // AES block size is 16 bytes (128 bits)

// Function to encrypt data
String encryptData(const String& data) {
    // Clear the buffer before encryption
    memset(buffer, 0, sizeof(buffer));
    
    // Perform AES encryption
    aes.do_aes_encrypt((byte*)data.c_str(), data.length(), (byte*)buffer, (byte*)secretKey, 128);
    
    // Convert encrypted bytes to a hex string for display
    String encryptedData = "";
    for (int i = 0; i < 16; i++) { // AES block size
        char hexStr[3];
        sprintf(hexStr, "%02X", (byte)buffer[i]); // Convert to hex
        encryptedData += hexStr; // Append hex string
    }
    
    return encryptedData;
}

// Function to decrypt data
String decryptData(const String& data) {
    // Convert hex string back to bytes
    for (int i = 0; i < 16; i++) {
        String byteString = data.substring(i * 2, i * 2 + 2); // Get hex pair
        buffer[i] = (char) strtol(byteString.c_str(), NULL, 16); // Convert hex to byte
    }

    // Clear the original data before decryption
    char decrypted[32];
    memset(decrypted, 0, sizeof(decrypted));
    
    // Perform AES decryption
    aes.do_aes_decrypt((byte*)buffer, sizeof(buffer), (byte*)decrypted, (byte*)secretKey, 128);
    
    return String(decrypted); // Return decrypted string
}

void setup() {
    Serial.begin(9600);
    
    String originalData = "Hello IoT!";
    Serial.print("Original Data: ");
    Serial.println(originalData);

    // Encrypt the original data
    String encryptedData = encryptData(originalData);
    Serial.print("Encrypted Data: ");
    Serial.println(encryptedData);

    // Decrypt the encrypted data
    String decryptedData = decryptData(encryptedData);
    Serial.print("Decrypted Data: ");
    Serial.println(decryptedData);
}

void loop() {
    // No operation in loop
}