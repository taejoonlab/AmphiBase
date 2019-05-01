#!/bin/bash
GENOME_CODE='xenTro9'
rsync -avzP rsync://hgdownload.soe.ucsc.edu/goldenPath/$GENOME_CODE/bigZips/ .
rsync -avzP rsync://hgdownload.soe.ucsc.edu/goldenPath/$GENOME_CODE/database .
rsync -avzP rsync://hgdownload.soe.ucsc.edu/goldenPath/$GENOME_CODE/vsHg38 .
rsync -avzP rsync://hgdownload.soe.ucsc.edu/goldenPath/$GENOME_CODE/vsXenLae2 .
