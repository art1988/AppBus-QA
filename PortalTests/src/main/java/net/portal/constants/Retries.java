package net.portal.constants;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

public class Retries {
    public static final Retry RETRY_50_TIMES = new SimpleRetry(50); //about 15 mins
    public static final Retry RETRY_10_TIMES = new SimpleRetry(10); //about 3 mins
    public static final Retry RETRY_04_TIMES = new SimpleRetry(1); //for debugging, 10-15 sec
    public static final Retry RETRY_01_TIMES = new SimpleRetry(1); //for debugging, 10-15 sec

    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");

    private Retries() {
    }

    public interface Retry {
        void run(Runnable runnable);
    }

    public static class SimpleRetry implements Retry {
        private final int retryNum;

        public SimpleRetry(int retryNum) {
            this.retryNum = retryNum;
        }

        @Override
        public void run(Runnable runnable) {
            for (int i = 0; i < retryNum; i++) {
                try {
                    if (i == 1) {
                        System.out.println("Retries: the second Try, runnable.getClass().toString() is: " + runnable.getClass().toString());
                        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
                        String mdhms = df.format(timeMDHMS);
                        System.out.println("current time is: " + mdhms);
                    }
                    runnable.run();
                    if (i != 0) {
                        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
                        String mdhms = df.format(timeMDHMS);
                        System.out.println("Success from Retries.java, iteration #: " + i + ", current time is: " + mdhms);
                    }
                    break;
                } catch (Exception e) {
                    if (i == (retryNum - 1)) {
                        /* e.printStackTrace(); */
                        System.out.println("Retries: the last Try #: " + retryNum + "Method : " + runnable.toString());
                        Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
                        String mdhms = df.format(timeMDHMS);
                        System.out.println("current time is: " + mdhms);
                        throw e;
                    }
                    try {
                        Thread.sleep(500L);
                    } catch (InterruptedException ex) {
                        break;
                    }
                }
            }
        }
    }
}
