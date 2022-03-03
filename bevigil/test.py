from .Enumerator import BeVigil
import json

bevigil = BeVigil(api_key = "oa6ckC3TRE00RdUM")
# data = bevigil.getPackagesFromSubdomain(subdomain = "support.apple.com")

# data = bevigil.getSubdomainsFromDomain(domain = "petronas.com.my")

# data = bevigil.getUrlsFromDomain(domain = "petronas.com.my")

# data = bevigil.getS3bucketsFromKeyword(keyword = "paytm")

# data = bevigil.getWordlistFromPackage(package_id = "com.siftwallet.sift.android")

# data = bevigil.getHostsFromPackage(package_id = "com.siftwallet.sift.android")

# data = bevigil.getS3bucketsFromPackage(package_id = "com.siftwallet.sift.android")

data = bevigil.validateKey()

print(json.dumps(data , indent = 3))
