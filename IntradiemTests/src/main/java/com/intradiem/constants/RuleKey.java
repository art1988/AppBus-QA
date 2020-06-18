package com.intradiem.constants;

public enum RuleKey
{
    COMMENT("comment"),
    REQUEST("request"),
    HEADER("header"),
    BODY("body");

    private final String key;

    RuleKey(final String key)
    {
        this.key = key;
    }

    public String getKey()
    {
        return key;
    }
}
