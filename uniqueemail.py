class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        result = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            result.add(local.replace('.','') + '@' + domain)
        return len(result)