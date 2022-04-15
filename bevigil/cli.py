import json
import os
import click

from .enumerator import BeVigil
from .exceptions import InvalidAPIKeyError, APIError
from .helpers import getAPIKey
from .settings import BEVIGIL_CONFIG_DIR

# To enable both --help and -h to show help message
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """\x1b[0;34m██████╗░███████╗██╗░░░██╗██╗░██████╗░██╗██╗░░░░░  ░█████╗░██╗░░░░░██╗
██╔══██╗██╔════╝██║░░░██║██║██╔════╝░██║██║░░░░░  ██╔══██╗██║░░░░░██║
██████╦╝█████╗░░╚██╗░██╔╝██║██║░░██╗░██║██║░░░░░  ██║░░╚═╝██║░░░░░██║
██╔══██╗██╔══╝░░░╚████╔╝░██║██║░░╚██╗██║██║░░░░░  ██║░░██╗██║░░░░░██║
██████╦╝███████╗░░╚██╔╝░░██║╚██████╔╝██║███████╗  ╚█████╔╝███████╗██║
╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░╚═════╝░╚═╝╚══════╝  ░╚════╝░╚══════╝╚═╝\x1b[0m\n

bevigil-cli is a tool for querying OSINT API of BeVigil for asset extraction"""


@cli.group()
def enum():
    """Enumerate assets using BeVigil OSINT API"""
    pass


@cli.command("init")
@click.option("--api-key", help="API Key to use", type=str, metavar="<API Key>", required=True)
@click.option("--autocomplete" , help = "Enable commands and options autocompletion" , is_flag = True , required = False)
def init(api_key , autocomplete):
    """Initialize bevigil-cli using API key"""
    # Creating config directory
    bevigil_dir = os.path.expanduser(BEVIGIL_CONFIG_DIR)
    if not os.path.isdir(bevigil_dir):
        try:
            os.makedirs(bevigil_dir)
        except OSError:
            raise click.ClickException("Unable to create BeVigil configuration directory")

    # Checking if the API key is valid
    api_key = api_key.strip()
    bevigil = BeVigil(api_key=api_key)
    if not bevigil.validateKey():
        raise click.ClickException("Invalid API key")

    # Store the API key in config dir if valid
    api_key_file = bevigil_dir + "/api_key"
    with open(api_key_file, "w") as file_obj:
        file_obj.write(api_key)
        click.echo(click.style("API key successfully configured", fg="green"))

    # Make the file read only
    os.chmod(api_key_file, 0o600)

    # For autocompletion
    if autocomplete:
        autocomplete_shell_map = {
            "bash" : {
                "path" : os.path.expanduser("~/.bashrc") ,
                "command" : 'eval "$(_BEVIGIL_CLI_COMPLETE=bash_source bevigil-cli)"'
            } ,
            "zsh" : {
                "path" : os.path.expanduser("~/.zshrc") ,
                "command" : 'eval "$(_BEVIGIL_CLI_COMPLETE=zsh_source bevigil-cli)"'
            } ,
            "fish" : {
                "path" : os.path.expanduser("~/.config/fish/completions/foo-bar.fish") ,
                "command" : 'eval (env _BEVIGIL_CLI_COMPLETE=fish_source bevigil-cli)'
            }
        }
        shell = os.environ["SHELL"]
        shell_file = ""
        shell_payload = ""
        
        if "bash" in shell:
            shell_file = autocomplete_shell_map["bash"]["path"]
            shell_payload = autocomplete_shell_map["bash"]["command"]
        elif "zsh" in shell:
            shell_file = autocomplete_shell_map["zsh"]["path"]
            shell_payload = autocomplete_shell_map["zsh"]["command"]
        elif "fish" in shell:
            shell_file = autocomplete_shell_map["fish"]["path"]
            shell_payload = autocomplete_shell_map["fish"]["command"]
        else:
            raise click.ClickException(click.style("Unsupported shell for autocompletion" , fg = "yellow"))

        # Write entry in the shell file
        try:
            with open(shell_file , "a") as rc_file:
                rc_file.write("# For bevigil-cli command automation\n")
                rc_file.write(shell_payload + "\n")
        except Exception:
            raise click.ClickException(click.style(f"Unable to write {shell_file}" , fg = "red"))
        
        click.echo(click.style("Command autocompletion enabled, Please restart your terminal" , fg = "yellow"))


@enum.command("packages", short_help="Request packages associated associated with a domain/subdomain")
@click.option("--domain", type=str, help="domain", metavar="<domain>")
@click.option("--subdomain", type=str, help="subdomain", metavar="<subdomain>")
def getPackages(domain, subdomain):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        if domain:
            packages = bevigil.getPackagesFromDomain(domain=domain)
        elif subdomain:
            packages = bevigil.getPackagesFromSubdomain(subdomain=subdomain)
        else:
            raise click.ClickException("Please specify either domain or subdomain to enumerate packages for")
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(packages, indent=3))


@enum.command("wordlist", short_help="Request a wordlist for a package")
@click.option("--package", type=str, help="Package to request wordlist for", metavar="<Package ID>", required=True)
def getWordlist(package):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        wordlist = bevigil.getWordlistFromPackage(package_id=package)
    except APIError as err:
        raise click.ClickException(err.msg)
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(wordlist, indent=3))


@enum.command("hosts", short_help="Request hosts present in an android package")
@click.option("--package", type=str, help="Package to request hosts for", metavar="<Package ID>", required=True)
def getHosts(package):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        hosts = bevigil.getHostsFromPackage(package_id=package)
    except APIError as err:
        raise click.ClickException(err.msg)
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(hosts, indent=3))


@enum.command("s3", short_help="Request S3 buckets associated with a package or a keyword")
@click.option("--package", type=str, help="Package to request S3 buckets information for", metavar="<Package ID>")
@click.option("--keyword", type=str, help="Keyword to request S3 buckets information for", metavar="<Keyword>")
def getS3(package, keyword):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        if package:
            buckets = bevigil.getS3bucketsFromPackage(package_id=package)
        elif keyword:
            buckets = bevigil.getS3bucketsFromKeyword(keyword=keyword)
        else:
            raise click.ClickException("Please specify --package/--keyword for requesting S3 buckets")
    except APIError as err:
        raise click.ClickException(err.msg)
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(buckets, indent=3))


@enum.command("params", short_help="Request params associated with an android package")
@click.option("--package", type=str, help="Package to request params for", metavar="<Package ID>", required=True)
def getParams(package):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        params = bevigil.getParamsFromPackage(package_id=package)
    except APIError as err:
        raise click.ClickException(err.msg)
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(params, indent=3))


@enum.command("subdomains", short_help="Request subdomains associated with a domain")
@click.option("--domain", type=str, help="Domain to request Subdomains for", metavar="<Domain>", required=True)
def getSubdomains(domain):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        subdomains = bevigil.getSubdomainsFromDomain(domain=domain)
    except APIError as err:
        raise click.ClickException(err.msg)
    print(json.dumps(subdomains, indent=3))


@enum.command("urls", short_help="Request URLs associated with a domain")
@click.option("--domain", type=str, help="Domain to request URLs for", metavar="<Domain>", required=True)
def getURLs(domain):
    api_key = getAPIKey()
    bevigil = BeVigil(api_key=api_key)
    try:
        urls = bevigil.getUrlsFromDomain(domain=domain)
    except APIError as err:
        raise click.ClickException(err.msg)
    except InvalidAPIKeyError:
        raise click.ClickException("Invalid API Key")
    print(json.dumps(urls, indent=3))


def main():
    cli()


if __name__ == "__main__":
    main()
