/*

The unsigned transaction of setAccount Property (test1, value1):

{
    "transactionJSON": {
        "senderPublicKey": "6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19",
        "feeNQT": "100000000",
        "type": 1,
        "version": 1,
        "phased": false,
        "ecBlockId": "6827938886709383368",
        "attachment": {
            "property": "test1",
            "value": "value1",
            "version.AccountProperty": 1
        },
        "senderRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "subtype": 10,
        "amountNQT": "0",
        "sender": "15019823959905333982",
        "recipientRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "recipient": "15019823959905333982",
        "ecBlockHeight": 1556740,
        "deadline": 1,
        "timestamp": 127003043,
        "height": 2147483647
    },
    "unsignedTransactionBytes": "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c11700c89063d23db6c15e010574657374310676616c756531",
    "broadcasted": false,
    "requestProcessingTime": 10
}

The signed transaction :

{
    "signatureHash": "4892f9904048c1a2ddd3125340b4e068255c284ff52e5f462d8527fa213559c3",
    "transactionJSON": {
        "senderPublicKey": "6282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19",
        "signature": "2719adcbd0bb05831a2450bf3c4890e27a6560baa2323273260199f6ba8bb0099d2ea4e9225c6f02dbf8a882dbc92283f56de247189d3c2f9ee1082bd243f526",
        "feeNQT": "100000000",
        "type": 1,
        "fullHash": "9338130cf38d7055f25d8c2eeb5bafc3dcc9bd6f9ac224956fc45ff70314da23",
        "version": 1,
        "phased": false,
        "ecBlockId": "6827938886709383368",
        "signatureHash": "4892f9904048c1a2ddd3125340b4e068255c284ff52e5f462d8527fa213559c3",
        "attachment": {
            "property": "test1",
            "value": "value1",
            "version.AccountProperty": 1
        },
        "senderRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "subtype": 10,
        "amountNQT": "0",
        "sender": "15019823959905333982",
        "recipientRS": "NXT-XWQY-C2MJ-JPL8-F4BW2",
        "recipient": "15019823959905333982",
        "ecBlockHeight": 1556740,
        "deadline": 1,
        "transaction": "6156576765634623635",
        "timestamp": 127003043,
        "height": 2147483647
    },
    "verify": true,
    "requestProcessingTime": 12,
    "transactionBytes": "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f5050000000000000000000000000000000000000000000000000000000000000000000000002719adcbd0bb05831a2450bf3c4890e27a6560baa2323273260199f6ba8bb0099d2ea4e9225c6f02dbf8a882dbc92283f56de247189d3c2f9ee1082bd243f5260000000004c11700c89063d23db6c15e010574657374310676616c756531",
    "fullHash": "9338130cf38d7055f25d8c2eeb5bafc3dcc9bd6f9ac224956fc45ff70314da23",
    "transaction": "6156576765634623635"
}

*/

package alessiotest;

import java.io.UnsupportedEncodingException;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

class TestUnsigned {
  public static void main(String[] args){
    String secretPhrase = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider";
    String message = "Messaggio di prova";
    String unsignedTransactionBytes = "011aa3e9910701006282332ff83fb3ce267157e5a7d04921f0b7f719aad5bf2117561c2ca7850d19def20e27502271d0000000000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c11700c89063d23db6c15e010574657374310676616c756531";

    boolean KeyProcedure = true;
    boolean SignProcedure = false;

    byte[] pb;
    byte[] si;

    byte[] utb;

        utb = parseHexString(unsignedTransactionBytes);
        // utb = unsignedTransactionBytes.getBytes("UTF-8");
        System.out.println("bytes "+utb);

    Crypto t = new Crypto();

    if(KeyProcedure) {
        System.out.println("Utb  --> "+utb);

        pb = t.getPublicKey(secretPhrase);

        String pluto = toHexString(pb);
        System.out.println("##################### Public Key  --> "+pluto);

    }
    if(SignProcedure) {
        si = t.sign(utb, secretPhrase);
        String ciro = toHexString(si);

        byte[] ciro2 = parseHexString(ciro);


        System.out.println("Signed transaction  --> "+si);
        String encoded = Base64.getEncoder().encodeToString(si);
        System.out.println("Base 64 Signed transaction  --> "+encoded);
        System.out.println("Signed transaction  getHex      --> "+getHex(si));
        System.out.println("Signed transaction  toHexString --> "+toHexString(si));
        System.out.println("Signed transaction  parseHexString --> "+parseHexString(ciro));
        System.out.println(ciro2);
        System.out.println("Signed transaction toHexString (ciro2) --> "+toHexString(ciro2));

        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            // byte[] hash = digest.digest(text.getBytes(StandardCharsets.UTF_8));
            byte[] sihashed = digest.digest(si);
            System.out.println("Hased Signed transaction  --> "+sihashed);
        } catch (NoSuchAlgorithmException e) {
                throw new RuntimeException(e);      // Never happen.
        }


        si = t.sign(parseHexString(unsignedTransactionBytes), secretPhrase);
    }
}

static final String HEXES = "0123456789abcdef";
private static final char[] hexChars = { '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f' };

public static String getHex( byte [] raw ) {
    if ( raw == null ) {
      return null;
    }
    final StringBuilder hex = new StringBuilder( 2 * raw.length );
    for ( final byte b : raw ) {
      hex.append(HEXES.charAt((b & 0xF0) >> 4))
         .append(HEXES.charAt((b & 0x0F)));
    }
    return hex.toString();
}

  /**
     * Parse a hex string and return the decoded bytes
     *
     * @param       hex                     String to parse
     * @return                              Decoded bytes
     * @throws      NumberFormatException   String contains an invalid hex character
     */
public static byte[] parseHexString(String hex) {
            if ((hex.length()&0x01) == 1)
                throw new NumberFormatException("Hex string length is not a multiple of 2");
            byte[] bytes = new byte[hex.length() / 2];
            for (int i = 0; i < bytes.length; i++) {
                int char1 = hex.charAt(i * 2);
                // System.out.println(char1+" "+hex.charAt(i * 2) );
                char1 = char1 > 0x60 ? char1 - 0x57 : char1 - 0x30;
                int char2 = hex.charAt(i * 2 + 1);
                // System.out.println(char2+" "+hex.charAt(i * 2 + 1));
                char2 = char2 > 0x60 ? char2 - 0x57 : char2 - 0x30;
                if (char1 < 0 || char2 < 0 || char1 > 15 || char2 > 15)
                    throw new NumberFormatException("Invalid hex number: " + hex);
                bytes[i] = (byte)((char1 << 4) + char2);
            }
            return bytes;
}

    /**
     * Convert a byte array to a hex string
     *
     * @param       bytes                   Bytes to encode
     * @return                              Hex string
     */
public static String toHexString(byte[] bytes) {
        char[] chars = new char[bytes.length * 2];
        for (int i = 0; i < bytes.length; i++) {
            chars[i * 2] = hexChars[((bytes[i] >> 4) & 0xF)];
            chars[i * 2 + 1] = hexChars[(bytes[i] & 0xF)];
        }
        return String.valueOf(chars);
}

}