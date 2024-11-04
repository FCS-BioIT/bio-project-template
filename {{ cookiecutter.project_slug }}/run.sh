WORKDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SNAKEDIR=$(realpath -m "$WORKDIR/src/Snakefile")
CONFIGDIR=$(realpath -m "$WORKDIR/config/snakemake-profile")

snakemake -d $WORKDIR \
	  -s $SNAKEDIR \
	  --workflow-profile $CONFIGDIR
