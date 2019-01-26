// package buffer.endian;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

/**
 *  * @author dzh
 *   *
 *    */
public class ByteOrderTest {
	public static void main(String[] args) {
		ByteBuffer buf =ByteBuffer.allocate(8);
		System.out.println("Default java endian: "+buf.order().toString()); 
/*
		buf.putShort((short) 2);
		buf.order(ByteOrder.LITTLE_ENDIAN);
		System.out.println("Now: "+buf.order().toString());
		buf.putShort((short)0x100);

		// buf = buf << 1;

		buf.flip();
		// for(int i=0;i<buf.limit();i++)
		//	System.out.println(buf.get()&0xFF); 
*/
		// buf.order(ByteOrder.LITTLE_ENDIAN);
		System.out.println("Now: "+buf.order().toString());
		// unsigned char sdata[5] = {0x93, 0x88, 0xB1, 0x18, 0x01};
		//
		/*
		long date = (long)0x0118B18893L;
		buf.putLong(date);
		// System.out.println("Limit: "+buf.limit());
		buf.flip();
		for (int i=0; i<5; i++)
			System.out.println(buf.get() & 0xFF);
		*/

		buf.put((byte)0x93);
		buf.put((byte)0x88);
		buf.put((byte)0xB1);
		buf.put((byte)0x18);
		buf.put((byte)0x01);
		buf.put((byte)0);
		buf.put((byte)0);
		buf.put((byte)0);
		buf.flip();
		// for (int i=0; i<5; i++)
		//	System.out.println(buf.get() & 0xFF);

		long tar = buf.getLong(0);
		int year = 2000 + (byte)(tar & 0x7F);
		byte month = (byte)((tar >> 7) & 0xF);
		byte day = (byte)((tar >> 11) & 0x1F);
		byte hour = (byte)((tar >> 16) & 0x1F);
		byte minute = (byte)((tar >> 22) & 0x3F);
		byte second = (byte)((tar >> 28) & 0x3F);
		System.out.println("" + year + "/" + month + "/" + day + " " + hour + ":" + minute + ":" + second);

		System.out.println("My PC: "+ByteOrder.nativeOrder().toString());
	}
}
