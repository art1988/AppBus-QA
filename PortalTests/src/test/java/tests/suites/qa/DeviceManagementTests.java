package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,

//Vitaly's tests:
        UserDevicesTabsAvailability.class, //C18004 (was C3094) case on testrail
        UserDevicesFindDevicesCheck.class, //C18005 (was C3095) case on testrail //Datasensitive case
        UserDevicesOSversionsCheck.class, //C18006 (was C3096) case on testrail //Datasensitive case
        RenewConfigsViaUploadingNewBoth.class, //for precondition of further cases
        ProvisionConfigAddRevertCheck.class, //C18007 (was C2364) case on testrail
        ProvisionConfigAddEmptyConfig.class, //C18013 (was C2365) case on testrail
        ProvisionConfigDeleteConfig.class, //C18014 (was C2366) case on testrail
        ProvisionConfigCreateCertN1.class, //C18024 (was C2367) case on testrail
        ProvisionConfigCreateCertN2.class, //C18025 (was C2368) case on testrail
        ProvisionConfigCreateCertN3.class, //C18026 (was C2369) case on testrail
        ProvisionConfigCreateCertN6.class, //C18027 (was C2370) case on testrail
//ED-4146        ProvisionConfigCreateCertAndGateways.class, //C18028 (was C2747) case on testrail
//ED-4146        ProvisionConfigCrCertGatewayService.class, //C18029 (was C2748) case on testrail //ED-4146
//ED-4146        ProvisionConfigApplyConfig.class, //C18030 + C18031 (was C2749 + C2750) case on testrail //ED-4146
//ED-4146        ProvisionConfigDiscardChanges.class, //C18032 (was C2751) case on testrail //ED-4146
//ED-4146        ProvisionConfigSaveUpcoming.class, //C18093 (was C2752) + C18151 (was C2767) case on testrail //ED-4146
        ProvisionConfigUploadUpcomingDiscard.class, //C18094 (was C2753) case on testrail
        ProvisionConfigUploadUpcomingSave.class, //C18095 (was C2764) case on testrail
        ProvisionConfigCopyCurrentConfig.class, //C18096 (was C2765) case on testrail
        ProvisionConfigDelCertFromUpcomn.class, //C18150 (was C2766) case on testrail
        ProvisionConfigDelServFromUpcomn.class, //C18152 (was C2768) case on testrail
        ProvisionConfigEditServicesUpcom.class, //C18159 (was C2769) case on testrail
        ProvisionConfigEditGatewayUpcom.class, //C19229 (was C2770) case on testrail  //Datasensitive, need previos case
        ProvisionConfigEditCertifiUpcom.class, //C20044 (was C2771) case on testrail
        ProvisionConfigDownloadCurrentC.class, //C20187 (was C2925) case on testrail
        ProvisionConfigDownloadCertOfCr.class, //C20188 (was C2926) case on testrail
//ED-4196        ProvisionConfigDeleteExpiredCon.class, //C20192 (was C2929) case on testrail  //todo: add check parms after ED-4213 fix
        ProvisionConfigMakeUpExpiredCon.class, //C20190 (was C2928) case on testrail //todo: add check parms after ED-4213 fix
        ProvisionConfigDeleteCurrentCon.class, //C20189 (was C2927) case on testrail
        RenewConfigsViaUploadingNewBoth.class, //for precondition of further cases
        ProvisionConfigMakeUpComToCurre.class, //C20193 (was C3069) case on testrail
        ProvisionConfigCrtCertInCurrent.class, //C20627 (was C3070) case on testrail
        ProvisionConfigCrtCertInCurren2.class, //C20771 (was C3075) case on testrail
        ProvisionConfigCrtCertInCurren1.class, //C20699 (was C3074) case on testrail
        ProvisionConfigCrtCertInCurren5.class, //C21839 (was C3076) case on testrail
})

public class DeviceManagementTests  extends ChromeHeadlessInternalQASetup
{

}
