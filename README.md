# check_ssl_certs
script to check ssl certificate info

requires pyopenssl

config file:
```
{
  "hosts": {
    "www.bing.com": 443,
    "www.yahoo.com": 443,
    "www.google.com": 443
  }
}
```

Usage:
```
▶ ./ssl_check.py -c certs.json

www.google.com
-----------
Common Name: www.google.com
Signature Algorithm: sha256WithRSAEncryption
Expiration: 10/27/2016 17:58:00

Common Name: Google Internet Authority G2
Signature Algorithm: sha256WithRSAEncryption
Expiration: 12/31/2017 23:59:59

Common Name: GeoTrust Global CA
Signature Algorithm: sha1WithRSAEncryption
Expiration: 08/21/2018 04:00:00


www.bing.com
-----------
Common Name: www.bing.com
Signature Algorithm: sha256WithRSAEncryption
Expiration: 03/16/2018 18:05:29

Common Name: Microsoft IT SSL SHA2
Signature Algorithm: sha256WithRSAEncryption
Expiration: 05/07/2018 17:03:30


www.yahoo.com
-----------
Common Name: www.yahoo.com
Signature Algorithm: sha256WithRSAEncryption
Expiration: 10/30/2017 23:59:59

Common Name: Symantec Class 3 Secure Server CA - G4
Signature Algorithm: sha256WithRSAEncryption
Expiration: 10/30/2023 23:59:59

Common Name: VeriSign Class 3 Public Primary Certification Authority - G5
Signature Algorithm: sha1WithRSAEncryption
Expiration: 11/07/2021 23:59:59
```
