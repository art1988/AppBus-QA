package com.intradiem.constants;

public enum RuleArray
{
    MSG_WHITE("messageWhiteList"),
    MSG_BLACK("messageBlackList"),
    WS_WHITE("websocketWhiteList"),
    WS_BLACK("websocketBlackList");

    private final String arrayName;


    RuleArray(String arrayName)
    {
        this.arrayName = arrayName;
    }

    public String getArrayName()
    {
        return arrayName;
    }
}
