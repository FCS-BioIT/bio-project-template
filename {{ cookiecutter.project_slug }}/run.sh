WORKDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SNAKEDIR=$(realpath -m "$WORKDIR/src/Snakefile")

snakemake -d $WORKDIR \
	  -s $SNAKEDIR
