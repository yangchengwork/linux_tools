// package buffer.endian;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

/**
 *  * @author dzh
 *   *
 *    */
public class ByteOrderTest {
	public static void main(String[] args) {
		ByteBuffer buf =ByteBuffer.allocate(4);
		System.out.println("Default java endian: "+buf.order().toString()); 

		buf.putShort((short) 1);
		buf.order(ByteOrder.LITTLE_ENDIAN);
		System.out.println("Now: "+buf.order().toString());
		buf.putShort((short) 2);

		buf.flip();
		for(int i=0;i<buf.limit();i++)
			System.out.println(buf.get()&0xFF); 

		System.out.println("My PC: "+ByteOrder.nativeOrder().toString());
	}
}
