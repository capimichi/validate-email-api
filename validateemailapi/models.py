from pydantic import BaseModel

class EmailValidationRequest(BaseModel):
    email_address: str
    check_format: bool = True
    check_blacklist: bool = True
    check_dns: bool = True
    dns_timeout: int = 10
    check_smtp: bool = True
    smtp_timeout: int = 10
    smtp_helo_host: str = 'my.host.name'
    smtp_from_address: str = 'my@from.addr.ess'
    smtp_skip_tls: bool = False
    smtp_tls_context: None = None
    smtp_debug: bool = False

    def get_email_address(self):
        return self.email_address

    def get_check_format(self):
        return self.check_format

    def get_check_blacklist(self):
        return self.check_blacklist

    def get_check_dns(self):
        return self.check_dns

    def get_dns_timeout(self):
        return self.dns_timeout

    def get_check_smtp(self):
        return self.check_smtp

    def get_smtp_timeout(self):
        return self.smtp_timeout

    def get_smtp_helo_host(self):
        return self.smtp_helo_host

    def get_smtp_from_address(self):
        return self.smtp_from_address

    def get_smtp_skip_tls(self):
        return self.smtp_skip_tls

    def get_smtp_tls_context(self):
        return self.smtp_tls_context

    def get_smtp_debug(self):
        return self.smtp_debug

class EmailValidationResponse(BaseModel):
    is_valid: bool
