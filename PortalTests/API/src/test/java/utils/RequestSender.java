
package utils;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.util.EntityUtils;

import org.apache.http.conn.ssl.*;
import org.apache.http.impl.client.HttpClients;
import javax.net.ssl.*;
import java.io.FileInputStream;
import java.security.*;
import java.util.logging.Logger;

public class RequestSender {

	protected static final Logger logger = Logger.getLogger(RequestSender.class.getName());

	public static RequestSender requestSender;

	public RequestSender() {
	}

	public static RequestSender getInstance() {
		if (requestSender == null) {
			requestSender = new RequestSender();
		}
		return requestSender;
	}

	public String sendGet(String url) throws Exception {
		logger.info("Sending 'GET' request to URL : " + url);
		HttpClient httpClient = getClient();
		HttpGet get = new HttpGet(url);
		HttpResponse response = httpClient.execute(get);
		logger.info("Response Code : " + response.getStatusLine().getStatusCode());
		String responseBody = EntityUtils.toString(response.getEntity(), "UTF-8");
		response.getEntity().getContent().close();
		//logger.info("Response Body : " + responseBody);
		return responseBody;
	}

	public String sendPost(String url, String body) throws Exception {
		logger.info("Sending 'POST' request to URL : " + url);
		HttpPost post = new HttpPost(url);
		post.setHeader("Content-type", "application/json");
		post.setHeader("Accept", "application/json");
		logger.info("With body : " + body);
		post.setEntity(new StringEntity(body));
		HttpClient httpClient = getClient();
		HttpResponse response = httpClient.execute(post);
		logger.info("Response Code : " + response.getStatusLine().getStatusCode());
		String responseBody = EntityUtils.toString(response.getEntity(), "UTF-8");
		response.getEntity().getContent().close();
		return responseBody;
	}

	public String sendDel(String url) throws Exception {
		logger.info("Sending 'DEL' request to URL : " + url);
		HttpDelete delete = new HttpDelete(url);
		HttpClient httpClient = getClient();
		HttpResponse response = httpClient.execute(delete);
		logger.info("Response Code : " + response.getStatusLine().getStatusCode());
		if (response.getEntity() == null) return null;
		String responseBody = EntityUtils.toString(response.getEntity(), "UTF-8");
		response.getEntity().getContent().close();
		return responseBody;
	}

	private HttpClient getClient() throws Exception {
		String keyPassphrase = PropertyReader.getInstance().getProperty("certPassword", "Qalaborate");
		String certFileName = PropertyReader.getInstance().getProperty("certFileName", "Qalaborate.pfx");

//		KeyStore keyStore = KeyStore.getInstance("PKCS12");
//		keyStore.load(new FileInputStream(certFileName),
//				keyPassphrase.toCharArray());
//
//		SSLContext sslContext = SSLContexts.custom()
//				.loadKeyMaterial(keyStore, keyPassphrase.toCharArray())
//				.build();
//		HttpClient httpClient = HttpClients.custom().setSSLContext(sslContext)
//				.build();

		KeyStore keyStore = KeyStore.getInstance("PKCS12");
		keyStore.load(new FileInputStream(certFileName),
				keyPassphrase.toCharArray());

		SSLContext sslContext = SSLContexts.custom()
				.loadKeyMaterial(keyStore, keyPassphrase.toCharArray())
				.build();
		HttpClient httpClient = HttpClients.custom().setSSLContext(sslContext)
				.build();
		return httpClient;
	}

}
