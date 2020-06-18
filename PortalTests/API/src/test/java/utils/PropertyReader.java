package utils;

import java.io.*;
import java.util.HashMap;
import java.util.Properties;


public class PropertyReader {
	public static PropertyReader propertyReader;

	public PropertyReader() {
	}

	public static PropertyReader getInstance() {
		if (propertyReader == null) {
			propertyReader = new PropertyReader();
		}
		return propertyReader;
	}

	public String getProperty(String propertyName) {
		Properties props = getPropertiesObj();
		return props.getProperty(propertyName);
	}

	public String getProperty(String propertyName, String defaultValue) {
		Properties props = getPropertiesObj();

		return props.getProperty(propertyName, defaultValue);
	}

	private Properties getPropertiesObj() {
		Properties props = new Properties();
		FileReader fileReader = null;
		try {
			fileReader = new FileReader(System.getProperty("props"));
			props.load(fileReader);
		} catch (IOException e) {
			throw new RuntimeException("Unable to read property file");
		} finally {
			closeStream(fileReader);
		}
		return props;
	}

	private static void closeStream(Closeable stream) {
		if (stream == null) return;
		try {
			stream.close();
		} catch (IOException ignore) {
		}
	}
}
