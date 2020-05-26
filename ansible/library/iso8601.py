import datetime
from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(

        ),
        supports_check_mode=True
    )
    if module.check_mode:
        module.exit_json(changed=False)

    iso = datetime.datetime.now(tz=datetime.timezone.utc).isoformat(timespec='seconds')
    module.exit_json(changed=False, iso8601=iso)

if __name__ == '__main__':
    main()
