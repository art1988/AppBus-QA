package net.portal.constants;

public enum Notifications
{
    SUCCESSFULLY_ADDED("Successfully added."),
    SUCCESSFULLY_DELETED("Successfully deleted."),
    SUCCESSFULLY_SAVED("Successfully saved."),
    SUCCESSFULLY_UPDATED("Successfully updated."),
    SUCCESSFULLY_RELOADED("Successfully reloaded"),
    ENVIRONMENT_SHOULDNT_CONTAIN_WHITESPACES("Environment name shouldn't be empty or contain whitespaces."),
    CANT_REMOVE_CONTROLLER_TYPE("Can't remove controller types which are assigned to items or item properties:"),
    SETTING_ALREADY_EXISTS("Setting with specified group and name already exists."),
    STRATUM_NAME_SHOULD_BE_UNIQUE("Stratum name should be unique."),
    STRATUM_GROUP_NAME_SHOULD_BE_UNIQUE("Stratum group name should be unique."),
    ITEM_CONTEXT_NAME_SHOULD_BE_UNIQUE("Item context name should be unique."),
    GROUP_NEEDS_CONTAIN_AT_LEAST_ONE_STRATUM("Group needs contain at least one stratum."),
    JAVA_LIB_NAME_ALREADY_EXISTS("Java lib name already exists"),
    PROJECT_NAME_ALREADY_EXISTS("Project name already exists."),
    PROJECT_WAS_REMOVED("Project was removed."),
    DB_CONNECTION_WAS_SAVED("Db connection was saved"),
    TEST_SUCCESSFUL("Test successful"),
    DB_CONNECTION_NAME_ALREADY_EXISTS("Db connection name already exists"),
    DB_CONNECTION_WAS_REMOVED("Db connection was removed"),
    APPLICATION_NAME_SHOULD_BE_UNIQUE("Application name should be unique."),
    NAVIGATION_TREE_WAS_REGENERATED("Navigation tree was regenerated"),
    GROUP_WAS_SAVED("Group was saved."),
    GROUP_WAS_REMOVED("Group was removed."),
    PROPERTY_NAME_SHOULD_BE_UNIQUE("Property name should be unique."),
    POLICY_SUCCESSFULLY_SAVED("Policy successfully saved"),
    ROLE_NAME_SHOULD_BE_UNIQUE_FOR_ENVIRONMENT("Role name should be unique for environment."),
    SERVICE_WAS_REMOVED("Service was removed."),
    JOB_WAS_SUCCESSFULLY_REMOVED("Job was successfully removed"),
    UI_WAS_REMOVED("UI was removed."),
    UI_TITLE_ALREADY_EXISTS("UI title already exists."),
    ITEM_WAS_MOVED("Item was moved"),
    WERE_LOAD_5_RECORDS("Were load 5 records"),
    WERE_LOAD_1_RECORDS("Were load 1 records"),
    ITEM_WAS_REMOVED("Item was removed."),
    POOL_PROVIDER_WAS_SUCCESSFULLY_SAVED("Pool provider was successfully saved."),
    POOL_PROVIDER_NAME_ALREADY_EXISTS("Pool provider name already exists."),
    POOL_PROVIDER_WAS_SUCCESSFULLY_REMOVED("Pool provider was successfully removed."),
    EMAIL_GROUP_NAME_SHOULD_BE_UNIQUE("Email Group name should be unique."),
    FIELD_CLIENT_DROPDOWN_CANNOT_BE_EMPTY("Field 'Client dropdown:' cannot be empty."),
    SERVICE_WITH_THIS_NAME_ALREADY_EXISTS("Service with this name already exists."),
    UNABLE_TO_REMOVE_CERTIFICATE("Unable to remove certificate. Probably, it's used by one of gateways."),
    UNABLE_TO_REMOVE_GATEWAY("Unable to remove gateway. Probably, it's used by one of services."),
    INVALID_FORMAT_OR_VALUE("Invalid format or value (value must be less then 99999999 and more then 0)"),
    DATA_WERE_RELOADED_FROM_DB("Data were reloaded from DB"),
    CERTIFICATE_IS_EMPTY("Certificate is empty. Upload certificate first."),
    FIELD_NAME_CANNONT_BE_EMPTY("Field 'Name:' cannot be empty."),
    DATE_CANT_LESS_THAN_CURRENT("Date for the upcoming config can't be less than current.");

    private final String notificationText;


    Notifications(final String notificationText)
    {
        this.notificationText = notificationText;
    }

    public String getNotificationText()
    {
        return notificationText;
    }
}
