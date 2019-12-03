import re


# TODO: to many func args
def os_version_names_regex(versions_json, os):
    os_dict = versions_json[os]
    os_version_names = os_dict.keys()
    return "|".join(os_version_names)


def extract_version_number(versions_json, match, os):
    version_name = match.group()
    version_number = versions_json[os][version_name]
    version_number = str(version_number)
    return version_number


def os_parser(versions_json, snmp_data):
    KERNEL_VERSION_INDEX_IN_SPLITTED_SNMP_DATA = 2
    os = ""
    vendor = ""

    ubuntu_version_names_regex = os_version_names_regex(versions_json, 'ubuntu')
    ubuntu_match = re.search(ubuntu_version_names_regex, snmp_data)
    if ubuntu_match:
        # TODO: maybe ds instead of this assigning
        vendor = "canonical"
        os = "ubuntu"
        version_number = extract_version_number(versions_json, ubuntu_match, os)

    centos_version_names_regex = os_version_names_regex(versions_json, os='centos')
    centos_match = re.search(centos_version_names_regex, snmp_data)
    if centos_match:
        vendor = "centos"
        os = "centos"
        version_number = extract_version_number(versions_json, centos_match, os)

    kernel_version = snmp_data.split()[KERNEL_VERSION_INDEX_IN_SPLITTED_SNMP_DATA]

    parsed_dict = {
        "vendor": vendor, "os": os,
        "version_number": version_number, "kernel_version": kernel_version
    }

    return parsed_dict
