**Example configuration.yaml:**

```yaml
climate:
  platform: midea
  app_key: midea_app_api_key
  username: 'foo@bar.com'
  password: !secret midea_password
```

**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The platform name.
**app_key (Required)** | Midea app API key.
**username (Required)** | Username for Midea cloud.
**password (Required)** | Password for Midea cloud.
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only
