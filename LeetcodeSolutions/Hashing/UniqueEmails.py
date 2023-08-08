def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        hashset = set()
        for email in emails:
            localname, domainname = email.split("@")
            localname = localname.split("+")[0]
            localname = localname.replace(".", "")
            email = localname + "@" + domainname
            hashset.add(email)
        return len(hashset)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))