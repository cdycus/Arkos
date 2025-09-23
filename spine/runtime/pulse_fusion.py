def fuse_domain_outputs(*domain_results):
    all_results = []
    for domain in domain_results:
        if isinstance(domain, list):
            all_results.extend(domain)
        else:
            all_results.append(domain)
    return max(all_results, key=lambda x: x.get("confidence", 0))
