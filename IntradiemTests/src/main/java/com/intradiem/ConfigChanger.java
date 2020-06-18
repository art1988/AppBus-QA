package com.intradiem;

import com.intradiem.constants.Const;
import com.intradiem.constants.RuleArray;
import com.intradiem.constants.RuleKey;
import com.intradiem.helpers.Saver;
import org.apache.commons.io.FileUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.*;
import java.util.ArrayList;

public class ConfigChanger
{
    private JSONObject root;


    public ConfigChanger() throws IOException, ParseException
    {
        // read the json file
        FileReader reader = new FileReader(Const.DPA_CONFIG_PATH);

        JSONParser jsonParser = new JSONParser();

        root = (JSONObject) jsonParser.parse(reader);
    }

    /**
     * Remove single rule in arrayName found by comment
     * @param arrayName JSONArray can be messageWhiteList, messageBlackList, websocketWhiteList or websocketBlackList
     * @param comment of single rule
     * @throws IOException
     */
    public void removeRule(RuleArray arrayName, String comment) throws IOException
    {
        JSONArray array = (JSONArray) root.get(arrayName.getArrayName());

        int index = 0;
        for( Object o : array )
        {
            JSONObject singleRule = (JSONObject) o;

            String commentValue = String.valueOf(singleRule.get(RuleKey.COMMENT.getKey())),
                   headerValue  = String.valueOf(singleRule.get(RuleKey.HEADER.getKey())),
                   bodyValue    = String.valueOf(singleRule.get(RuleKey.BODY.getKey()));

            if( commentValue.equals(comment) )
            {
                array.remove(index);
                System.out.println("Rule with comment = " + commentValue + " was removed...");

                Saver.setHeaderOfRemovedRule(headerValue);
                Saver.setBodyOfRemovedRule(bodyValue);

                break;
            }

            index++;
        }

        // Save modified file
        FileWriter file = new FileWriter(Const.DPA_CONFIG_PATH);

        file.write(root.toString());
        file.flush();
        file.close();
    }

    /**
     * Restore dpa.config to previous state from copy (allow all rule)
     */
    public static void restoreDpaConfig() throws IOException
    {
        FileUtils.copyFile(new File(Const.DPA_CONFIG_COPY_PATH), new File(Const.DPA_CONFIG_PATH));
    }

    /**
     * Makes copy of dpa.config
     * @throws IOException
     */
    public void makeCopyOfDpaConfig() throws IOException
    {
        File dest = new File(Const.DPA_CONFIG_COPY_PATH);

        FileUtils.copyFile(new File(Const.DPA_CONFIG_PATH), dest);
    }

    /**
     * Does config contain comment ?
     * @param comment
     * @return
     */
    public static boolean contains(String comment) throws IOException
    {
        ArrayList<String> strings = (ArrayList) FileUtils.readLines(new File(Const.DPA_CONFIG_PATH), "UTF-8");

        for ( String s: strings )
        {
            if( s.contains(comment) )
            {
                return true;
            }
        }

        return false;
    }

}
