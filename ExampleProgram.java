package alessiotest;


class ExampleProgram {
  public static void main(String[] args){
    String secretPhrase = "pass dig enough trace frighten foul beaten explain knowledge yeah approach spider";
    String message = "Messaggio di prova";
    //String secretPhrase = "test";

    byte[] pb;
    Crypto t = new Crypto();

    pb = t.getPublicKey(secretPhrase);
    System.out.println("Public Key --> "+pb);


    StringBuilder sb = new StringBuilder();
    for (byte b : pb) {
        sb.append(String.format("%02X ", b));
    }

    System.out.println(sb.toString());
    System.out.println(pb);

    // System.out.println(Integer.toHexString(pb[0])+" "+Integer.toHexString(pb[1])+" "+Integer.toHexString(pb[2])+" "+Integer.toHexString(pb[3]));


    // long ciccio = -1106596071855577L;

    // System.out.println((byte)ciccio);
    // System.out.println((long)ciccio);
  }

  static final String HEXES = "0123456789ABCDEF";
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
}