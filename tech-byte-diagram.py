# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.storage import S3
from diagrams.sap.other import PlaceholderServiceName
from diagrams.sap.integration import IntegrationSuite
from diagrams.sap.database_datamanagement import SAPHANACloud
from diagrams.sap.database_datamanagement import ObjectStore
from diagrams.sap.security import IdentityProvisioning
from diagrams.sap.analytics import SAPAnalyticsCloud
from diagrams.sap.runtimes import CloudFoundryRuntime
from diagrams.sap.database_datamanagement import SAPHANACloud

# SAP BTP Solution Diagrams and Icons guidelines colours
L0_BLUE_COLOUR = "#0070F2"
L0_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#0040B0"
L1_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#002A86"
SUCCESS_GREEN_COLOUR = "#188918"
SUCCESS_FILLED_COLOUR = "#F5FAE5"

FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

with Diagram("CIS Landscape", show=False, outformat="jpg", filename="my_diagram"):
    with Cluster("SAP Cloud Identity Services (CIS)", graph_attr= {"bgcolor": L0_FILLED_COLOUR, "pencolor": L0_BLUE_COLOUR, "fontname": "Verdana", "fontsize": "16"}):
        with Cluster("SAP Cloud Identity Services - Identity Authentication (IAS)", graph_attr= {"bgcolor": "white", "pencolor": L1_BLUE_COLOUR, "fontname": "Verdana", "fontsize": "16"}):
            sap_ias_ino = IdentityProvisioning("CIS_SHELL_INO")

    with Cluster("Applications registered in CIS IAS"): 
        [SAPAnalyticsCloud("CISA_SAC_SACPREVIEW") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_DSPHERE_POC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_IPS_PERSONAS_POC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),

        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_SBX") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_INTS_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_ETM_NEXT_POC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_DSPHERE_POC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_BUILDAPPS_POC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_INO_SHELL_CF_OPEX_EU20") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        SAPHANACloud("CISA_HANADBCF_INO_SHELL_CF_HDB") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted")] >> sap_ias_ino
    
    # with Cluster("SAP Business Technology Platform", graph_attr= {"bgcolor": L0_FILLED_COLOUR, "pencolor": L0_BLUE_COLOUR}):
    #     with Cluster("Subaccount", graph_attr= {"bgcolor": "white", "pencolor": L1_BLUE_COLOUR}):
    #         cloud_integration = IntegrationSuite("Cloud Integration")
    #        object_store = ObjectStore("Object Store")

    #         PlaceholderServiceName("Audit Log service") << Edge(label="Retrieves entries", color=FIX_GREY_COLOUR) << \
    #         cloud_integration >> Edge(color=FIX_GREY_COLOUR) >> SAPHANACloud("HANA Cloud")
    #         cloud_integration >> Edge(color=FIX_GREY_COLOUR) >> object_store
        
    # with Cluster("AWS", graph_attr= {"bgcolor": "white", "pencolor": NON_SAP_AREA_COLOUR}):
    #     object_store >> Edge(label="uses", color=FIX_GREY_COLOUR, style="dotted") >> S3("S3 Bucket")
