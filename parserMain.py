
#!/usr/bin/python

import sys, getopt

import json, os


def main(argv):


  # os.system("export JAVA_HOME=/home/jdk-10.0.1/bin/java")

  # os.system("export PATH=$PATH:/home/jdk-10.0.1/bin")

   inputdir = ''
   outputdir = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["idir=","odir="])
   except getopt.GetoptError:
      print 'parserMain.py -i <inputdir> -o <outputdir>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'parserMain.py -i <inputdir> -o <outputdir>'
         sys.exit()
      elif opt in ("-o", "--odir"):
         outputdir = arg
      elif opt in ("-i", "--idir"):
         inputdir = arg

   metadata_path = inputdir + "/metadata.json"
   with open(metadata_path) as f:
      data = json.load(f)


   for dat in data:
      lcode = dat["lcode"]
      tcode = dat["tcode"]
	  
      if lcode == "grc" or lcode == "ro" or lcode == "lv" or tcode == "postwita" or lcode == "fa" or lcode == "tr" or lcode == "hu" or lcode == "he":
	  

         print(dat["psegmorfile"])
         conlluFile = dat["psegmorfile"]
         conllVersion = conlluFile[:-6]+"conll"
         TempConll = "temp-"+conlluFile[:-6]+"conll"

         outputConllu = dat["outfile"]
         outputConll = outputConllu[:-6]+"conll"

         trapath = "/media/training-datasets/universal-dependency-learning/conll18-ud-training-2018-05-06"
         devpath = inputdir

         os.system("perl preprocessing/conllu_to_conllx.pl < "+devpath+"/"+dat["psegmorfile"]+" > Temp/"+TempConll)

         os.system("perl -pe  's/_\t_\t_\t_\n/0\tdep\t_\t_\n/g' Temp/"+TempConll+" > Temp/"+conllVersion)


         dimension = 200

         if dat["lcode"] == "af" and dat["tcode"] == "afribooms":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "af_afribooms_parser_pos_2_200_100_20_200_12_20-pid10592.params"


         elif dat["lcode"] == "ar" and dat["tcode"] == "padt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Arabic/ar.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/ar.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ar.vectors --pretrained_dim 100 "
            modelFile = "ar_padt_embed_parser_pos_2_200_100_20_200_12_20-pid17030.params" #"ar_padt_parser_pos_2_200_100_20_200_12_20-pid28239.params"
            


         elif dat["lcode"] == "bg" and dat["tcode"] == "btb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "bg_btb_parser_pos_2_200_100_20_200_12_20-pid14824.params"


         elif dat["lcode"] == "bxr" and dat["tcode"] == "bdt":
            parserCode = "parser-ls/lstm-parse-ls"
            dimension = 200

            embeddingCode = ""
            modelFile = "bxr_bdt_parser_pos_2_200_100_20_200_12_20-pid17770.params"


         elif dat["lcode"] == "ca" and dat["tcode"] == "ancora":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Catalan/ca.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/ca.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ca.vectors --pretrained_dim 100 "
            modelFile = "ca_ancora_embed_parser_pos_2_200_100_20_200_12_20-pid25978.params" # "ca_ancora_parser_pos_2_200_100_20_200_12_20-pid26586.params"


         elif dat["lcode"] == "cs" and dat["tcode"] == "cac":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Czech/cs.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/cs.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/cs.vectors --pretrained_dim 100 "
            modelFile = "cs_cac_embed_parser_pos_2_200_100_20_200_12_20-pid20262.params" #"cs_cac_parser_pos_2_200_100_20_200_12_20-pid22981.params"


         elif dat["lcode"] == "cs" and dat["tcode"] == "fictree":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Czech/cs.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/cs.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/cs.vectors --pretrained_dim 100 "
            modelFile = "cs_fictree_embed_parser_pos_2_200_100_20_200_12_20-pid20443.params" #"cs_fictree_parser_pos_2_200_100_20_200_12_20-pid5213.params"


         elif dat["lcode"] == "cs" and dat["tcode"] == "pdt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "cs_pdt_parser_pos_2_200_100_20_200_12_20-pid11970.params"


         elif dat["lcode"] == "cu" and dat["tcode"] == "proiel":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Old_Church_Slavonic/cu.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/cu.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/cu.vectors --pretrained_dim 100 "
            modelFile = "cu_proiel_embed_parser_pos_2_200_100_20_200_12_20-pid25330.params" #"cu_proiel_parser_pos_2_200_100_20_200_12_20-pid17952.params"



         elif dat["lcode"] == "da" and dat["tcode"] == "ddt":
            parserCode = "parser-ls/lstm-parse-ls"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Danish/da.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/da.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/da.vectors --pretrained_dim 100 "
            modelFile = "da_ddt_embed_parser_pos_2_200_100_20_200_12_20-pid1106.params" #"da_ddt_parser_pos_2_200_100_20_200_12_20-pid18073.params"


         elif dat["lcode"] == "de" and dat["tcode"] == "gsd":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/German/de.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/de.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/de.vectors --pretrained_dim 100 "
            modelFile = "de_gsd_embed_parser_pos_2_200_100_20_200_12_20-pid5755.params" #"de_gsd_upos_parser_pos_2_200_100_20_200_12_20-pid9985.params"


         elif dat["lcode"] == "el" and dat["tcode"] == "gdt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Greek/el.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/el.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/el.vectors --pretrained_dim 100 "
            modelFile = "el_gdt_embed_parser_pos_2_200_100_20_200_12_20-pid21966.params" #"el_gdt_parser_pos_2_200_100_20_200_12_20-pid13450.params"


         elif dat["lcode"] == "en" and dat["tcode"] == "ewt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/English/en.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/en.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/en.vectors --pretrained_dim 100 "
            modelFile = "en_ewt_embed_parser_pos_2_200_100_20_200_12_20-pid5754.params" #"en_ewt_parser_pos_2_200_100_20_200_12_20-pid20020.params"


         elif dat["lcode"] == "en" and dat["tcode"] == "gum":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/English/en.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/en.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/en.vectors --pretrained_dim 100 "
            modelFile = "en_gum_embed_parser_pos_2_200_100_20_200_12_20-pid7176.params" #"en_gum_parser_pos_2_200_100_20_200_12_20-pid20952.params"

         elif dat["lcode"] == "en" and dat["tcode"] == "lines":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/English/en.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/en.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/en.vectors --pretrained_dim 100 "
            modelFile = "en_lines_embed_parser_pos_2_200_100_20_200_12_20-pid7100.params" #"en_lines_parser_pos_2_200_100_20_200_12_20-pid21669.params"

         elif dat["lcode"] == "es" and dat["tcode"] == "ancora":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Spanish/es.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/es.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/es.vectors --pretrained_dim 100 "
            modelFile = "es_ancora_embed_parser_pos_2_200_100_20_200_12_20-pid7571.params" #"es_ancora_parser_pos_2_200_100_20_200_12_20-pid22355.params"

         elif dat["lcode"] == "et" and dat["tcode"] == "edt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Estonian/et.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/et.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/et.vectors --pretrained_dim 100 "
            modelFile = "et_edt_embed_parser_pos_2_200_100_20_200_12_20-pid8069.params" #"et_edt_parser_pos_2_200_100_20_200_12_20-pid22734.params"

         elif dat["lcode"] == "eu" and dat["tcode"] == "bdt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Basque/eu.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/eu.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/eu.vectors --pretrained_dim 100 "
            modelFile = "eu_bdt_embed_parser_pos_2_200_100_20_200_12_20-pid30437.params" #"eu_bdt_parser_pos_2_200_100_20_200_12_20-pid14584.params"

         elif dat["lcode"] == "fa" and dat["tcode"] == "seraji":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Persian/fa.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/fa.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/fa.vectors --pretrained_dim 100 "
            modelFile = "fa_seraji_embed_parser_pos_2_100_100_20_100_12_20-pid8013.params" #"fa_seraji_parser_pos_2_100_100_20_100_12_20-pid22958.params"

         elif dat["lcode"] == "fi" and dat["tcode"] == "ftb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Finnish/fi.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/fi.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/fi.vectors --pretrained_dim 100 "
            modelFile = "fi_ftb_embed_parser_pos_2_200_100_20_200_12_20-pid8118.params" #"fi_ftb_parser_pos_2_200_100_20_200_12_20-pid24391.params"

         elif dat["lcode"] == "fi" and dat["tcode"] == "tdt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Finnish/fi.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/fi.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/fi.vectors --pretrained_dim 100 "
            modelFile = "fi_tdt_embed_parser_pos_2_200_100_20_200_12_20-pid9675.params" #"fi_tdt_parser_pos_2_200_100_20_200_12_20-pid32219.params"

         elif dat["lcode"] == "fr" and dat["tcode"] == "gsd":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/French/fr.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/fr.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/fr.vectors --pretrained_dim 100 "
            modelFile = "fr_gsd_embed_parser_pos_2_200_100_20_200_12_20-pid30171.params" #"fr_gsd_parser_pos_2_200_100_20_200_12_20-pid27287.params"

         elif dat["lcode"] == "fr" and dat["tcode"] == "sequoia":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/French/fr.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/fr.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/fr.vectors --pretrained_dim 100 "
            modelFile = "fr_sequoia_embed_parser_pos_2_200_100_20_200_12_20-pid30260.params" #"fr_sequoia_parser_pos_2_200_100_20_200_12_20-pid28239.params"

         elif dat["lcode"] == "fr" and dat["tcode"] == "spoken":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "fr_spoken_parser_pos_2_200_100_20_200_12_20-pid31926.params"

         elif dat["lcode"] == "fro" and dat["tcode"] == "srcmf":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "fro_srcmf_parser_pos_2_200_100_20_200_12_20-pid32271.params"

         elif dat["lcode"] == "ga" and dat["tcode"] == "idt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "ga_idt_parser_pos_2_200_100_20_200_12_20-pid8184.params"

         elif dat["lcode"] == "gl" and dat["tcode"] == "ctg":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "gl_ctg_parser_pos_2_200_100_20_200_12_20-pid8340.params"

       #  elif dat["lcode"] == "gl" and dat["tcode"] == "treegal":
       #     parserCode = "parser/lstm-parse"
       #     dimension = 200
       #     os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Galician/gl.vectors.xz /mnt/data/embedding-files/")            
       #     os.system("unxz /mnt/data/embedding-files/gl.vectors.xz")
       #     embeddingCode = "-w /mnt/data/embedding-files/gl.vectors --pretrained_dim 100 "
       #     modelFile = "gl_treegal_embed_parser_pos_2_200_100_20_200_12_20-pid6469.params" #"gl_treegal_parser_pos_2_200_100_20_200_12_20-pid32219.params"

         elif dat["lcode"] == "got" and dat["tcode"] == "proiel":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "got_proiel_parser_pos_2_200_100_20_200_12_20-pid10637.params"

         elif dat["lcode"] == "grc" and dat["tcode"] == "perseus":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Ancient_Greek/grc.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/grc.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/grc.vectors --pretrained_dim 100 "
            modelFile = "grc_perseus_embed_parser_pos_2_200_100_20_200_12_20-pid2857.params" #"grc_perseus_parser_pos_2_200_100_20_200_12_20-pid15969.params"

         elif dat["lcode"] == "grc" and dat["tcode"] == "proiel":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Ancient_Greek/grc.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/grc.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/grc.vectors --pretrained_dim 100 "
            modelFile = "grc_proiel_embed_parser_pos_2_200_100_20_200_12_20-pid3325.params" #"grc_proiel_parser_pos_2_200_100_20_200_12_20-pid30149.params"

         elif dat["lcode"] == "he" and dat["tcode"] == "htb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Hebrew/he.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/he.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/he.vectors --pretrained_dim 100 "
            modelFile = "he_htb_embed_parser_pos_2_200_100_20_200_12_20-pid9778.params" #"he_htb_parser_pos_2_200_100_20_200_12_20-pid547.params"

         elif dat["lcode"] == "hi" and dat["tcode"] == "hdtb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "hi_hdtb_parser_pos_2_200_100_20_200_12_20-pid4104.params"

         elif dat["lcode"] == "hr" and dat["tcode"] == "set":
            parserCode = "parser/lstm-parse"
            dimension = 200
            # os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Croatian/hr.vectors.xz /mnt/data/embedding-files/")            
            # os.system("unxz /mnt/data/embedding-files/hr.vectors.xz")
            embeddingCode = "" #"-w /mnt/data/embedding-files/hr.vectors --pretrained_dim 100 "
            modelFile = "hr_set_parser_pos_2_200_100_20_200_12_20-pid10796.params" # "hr_set_embed_parser_pos_2_200_100_20_200_12_20-pid9950.params"

      #   elif dat["lcode"] == "hsb" and dat["tcode"] == "ufal":
      #      parserCode = "parser/lstm-parse"
      #      dimension = 200
      #      embeddingCode = ""
      #      modelFile = "hsb_ufal_parser_pos_2_200_100_20_200_12_20-pid22117.params"

         elif dat["lcode"] == "hu" and dat["tcode"] == "szeged":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Hungarian/hu.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/hu.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/hu.vectors --pretrained_dim 100 "
            modelFile = "hu_szeged_embed_parser_pos_2_200_100_20_200_12_20-pid10504.params" #"hu_szeged_parser_pos_2_200_100_20_200_12_20-pid11883.params"

         elif dat["lcode"] == "hy" and dat["tcode"] == "armtdp":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "hy_armtdp_parser_pos_2_200_100_20_200_12_20-pid12820.params"

         elif dat["lcode"] == "id" and dat["tcode"] == "gsd":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Indonesian/id.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/id.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/id.vectors --pretrained_dim 100 "
            modelFile = "id_gsd_embed_parser_pos_2_100_100_20_100_12_20-pid565.params" #"id_gsd_parser_pos_2_200_100_20_200_12_20-pid1327.params"

         elif dat["lcode"] == "it" and dat["tcode"] == "isdt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "it_isdt_parser_pos_2_200_100_20_200_12_20-pid2025.params"

         elif dat["lcode"] == "it" and dat["tcode"] == "postwita":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Italian/it.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/it.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/it.vectors --pretrained_dim 100 "
            modelFile = "it_postwita_embed_parser_pos_2_200_100_20_200_12_20-pid10628.params" #"it_postwita_parser_pos_2_200_100_20_200_12_20-pid13183.params"

         elif dat["lcode"] == "ja" and dat["tcode"] == "gsd":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100

            embeddingCode = ""
            modelFile = "ja_gsd_parser_pos_2_100_100_20_100_12_20-pid27560.params"

         elif dat["lcode"] == "kk" and dat["tcode"] == "ktb":
            parserCode = "parser-ls/lstm-parse-ls"
            dimension = 200
            #os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Kazakh/kk.vectors.xz /mnt/data/embedding-files/")            
            #os.system("unxz /mnt/data/embedding-files/kk.vectors.xz")
            embeddingCode = ""  #"-w /mnt/data/embedding-files/kk.vectors --pretrained_dim 100 "
            modelFile = "kk_ktb_parser_pos_2_200_100_20_200_12_20-pid18475.params" #"kk_ktb_embed_parser_pos_2_200_100_20_200_12_20-pid948.params" #

         elif dat["lcode"] == "kmr" and dat["tcode"] == "mg":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "kmr_mg_parser_pos_2_200_100_20_200_12_20-pid23339.params"

         elif dat["lcode"] == "ko" and dat["tcode"] == "gsd":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Korean/ko.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/ko.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ko.vectors --pretrained_dim 100 "
            modelFile = "ko_gsd_embed_parser_pos_2_100_100_20_100_12_20-pid25435.params" #"ko_gsd_parser_pos_2_100_100_20_100_12_20-pid28252.params"

         elif dat["lcode"] == "ko" and dat["tcode"] == "kaist":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Korean/ko.vectors.xz /mnt/data/embedding-files/")            
            os.system("unxz /mnt/data/embedding-files/ko.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ko.vectors --pretrained_dim 100 "
            modelFile = "ko_kaist_embed_parser_pos_2_100_100_20_100_12_20-pid25517.params" #"ko_kaist_parser_pos_2_100_100_20_100_12_20-pid28830.params"

         elif dat["lcode"] == "la" and dat["tcode"] == "ittb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Latin/la.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/la.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/la.vectors --pretrained_dim 100 "
            modelFile = "la_ittb_embed_parser_pos_2_200_100_20_200_12_20-pid18281.params" #"la_ittb_parser_pos_2_200_100_20_200_12_20-pid14621.params"

         elif dat["lcode"] == "la" and dat["tcode"] == "perseus":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Latin/la.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/la.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/la.vectors --pretrained_dim 100 "
            modelFile = "la_perseus_embed_parser_pos_2_200_100_20_200_12_20-pid19083.params" #"la_perseus_parser_pos_2_200_100_20_200_12_20-pid23945.params"

         elif dat["lcode"] == "la" and dat["tcode"] == "proiel":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Latin/la.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/la.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/la.vectors --pretrained_dim 100 "
            modelFile = "la_proiel_embed_parser_pos_2_200_100_20_200_12_20-pid18619.params" #"la_proiel_parser_pos_2_200_100_20_200_12_20-pid17019.params"

         elif dat["lcode"] == "lv" and dat["tcode"] == "lvtb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Latvian/lv.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/lv.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/lv.vectors --pretrained_dim 100 "
            modelFile = "lv_lvtb_embed_parser_pos_2_200_100_20_200_12_20-pid10051.params" #"lv_lvtb_parser_pos_2_200_100_20_200_12_20-pid5032.params"

         elif dat["lcode"] == "nl" and dat["tcode"] == "alpino":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Dutch/nl.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/nl.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/nl.vectors --pretrained_dim 100 "
            modelFile = "nl_alpino_embed_parser_pos_2_200_100_20_200_12_20-pid23682.params" #"nl_alpino_parser_pos_2_200_100_20_200_12_20-pid13579.params"

         elif dat["lcode"] == "nl" and dat["tcode"] == "lassysmall":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Dutch/nl.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/nl.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/nl.vectors --pretrained_dim 100 "
            modelFile = "nl_lassysmall_embed_parser_pos_2_200_100_20_200_12_20-pid24550.params" #"nl_lassysmall_parser_pos_2_200_100_20_200_12_20-pid14324.params"

         elif dat["lcode"] == "no" and dat["tcode"] == "bokmaal":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "no_bokmaal_parser_pos_2_200_100_20_200_12_20-pid26806.params"

         elif dat["lcode"] == "no" and dat["tcode"] == "nynorsk":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "no_nynorsk_parser_pos_2_200_100_20_200_12_20-pid27294.params"

         elif dat["lcode"] == "no" and dat["tcode"] == "nynorsklia":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "no_nynorsklia_parser_pos_2_200_100_20_200_12_20-pid28930.params"

         elif dat["lcode"] == "pl" and dat["tcode"] == "lfg":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "pl_lfg_parser_pos_2_200_100_20_200_12_20-pid25631.params"

         elif dat["lcode"] == "pl" and dat["tcode"] == "sz":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "pl_sz_parser_pos_2_200_100_20_200_12_20-pid26772.params"

         elif dat["lcode"] == "pt" and dat["tcode"] == "bosque":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Portuguese/pt.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/pt.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/pt.vectors --pretrained_dim 100 "
            modelFile = "pt_bosque_embed_parser_pos_2_200_100_20_200_12_20-pid17369.params" #"pt_bosque_parser_pos_2_200_100_20_200_12_20-pid4605.params"

         elif dat["lcode"] == "ro" and dat["tcode"] == "rrt":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Romanian/ro.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/ro.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ro.vectors --pretrained_dim 100 "
            modelFile = "ro_rrt_embed_parser_pos_2_200_100_20_200_12_20-pid10562.params" #"ro_rrt_parser_pos_2_200_100_20_200_12_20-pid16538.params"

         elif dat["lcode"] == "ru" and dat["tcode"] == "syntagrus":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Russian/ru.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/ru.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ru.vectors --pretrained_dim 100 "
            modelFile = "ru_syntagrus_embed_parser_pos_2_200_100_20_200_12_20-pid22081.params" #"ru_syntagrus_parser_pos_2_200_100_20_200_12_20-pid27925.params"

         elif dat["lcode"] == "ru" and dat["tcode"] == "taiga":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "ru_taiga_parser_pos_2_200_100_20_200_12_20-pid14516.params"

         elif dat["lcode"] == "sk" and dat["tcode"] == "snk":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Slovak/sk.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/sk.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/sk.vectors --pretrained_dim 100 "
            modelFile = "sk_snk_embed_parser_pos_2_200_100_20_200_12_20-pid25755.params"  #"sk_snk_parser_pos_2_200_100_20_200_12_20-pid16334.params"

         elif dat["lcode"] == "sl" and dat["tcode"] == "ssj":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Slovenian/sl.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/sl.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/sl.vectors --pretrained_dim 100 "
            modelFile = "sl_ssj_embed_parser_pos_2_200_100_20_200_12_20-pid3939.params" #"sl_ssj_parser_pos_2_200_100_20_200_12_20-pid17322.params"

         elif dat["lcode"] == "sl" and dat["tcode"] == "sst":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Slovenian/sl.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/sl.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/sl.vectors --pretrained_dim 100 "
            modelFile = "sl_sst_embed_parser_pos_2_200_100_20_200_12_20-pid4158.params" #"sl_sst_parser_pos_2_200_100_20_200_12_20-pid10463.params"

         elif dat["lcode"] == "sme" and dat["tcode"] == "giella":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "sme_giella_parser_pos_2_200_100_20_200_12_20-pid19631.params"

         elif dat["lcode"] == "sr" and dat["tcode"] == "set":
            parserCode = "parser/lstm-parse"
            dimension = 200
            embeddingCode = ""
            modelFile = "sr_set_parser_pos_2_200_100_20_200_12_20-pid14832.params"

         elif dat["lcode"] == "sv" and dat["tcode"] == "lines":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Swedish/sv.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/sv.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/sv.vectors --pretrained_dim 100 "
            modelFile = "sv_lines_embed_parser_pos_2_200_100_20_200_12_20-pid21117.params" #"sv_lines_parser_pos_2_200_100_20_200_12_20-pid19641.params"

         elif dat["lcode"] == "sv" and dat["tcode"] == "talbanken":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Swedish/sv.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/sv.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/sv.vectors --pretrained_dim 100 "
            modelFile = "sv_talbanken_embed_parser_pos_2_200_100_20_200_12_20-pid21332.params" #"sv_talbanken_parser_pos_2_200_100_20_200_12_20-pid20783.params"

         elif dat["lcode"] == "tr" and dat["tcode"] == "imst":
            parserCode = "parser-ls/lstm-parse-ls"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Turkish/tr.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/tr.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/tr.vectors --pretrained_dim 100 "    #"-w /media/data/embeddings/wiki.tr.vec --pretrained_dim 300"
            modelFile = "tr_imst_embed_new_parser_pos_2_200_100_20_200_12_20-pid13691.params" # "tr_imst_embed_parser_pos_2_200_100_20_200_12_20-pid18285.params" #"tr_imst_parser_pos_2_200_100_20_200_12_20-pid27600.params"
                       
         elif dat["lcode"] == "ug" and dat["tcode"] == "udt":
            parserCode = "parser-ls/lstm-parse-ls"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Uyghur/ug.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/ug.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ug.vectors --pretrained_dim 100 " 
            modelFile = "ug_udt_embed_parser_pos_2_200_100_20_200_12_20-pid1364.params" #"ug_udt_parser_pos_2_200_100_20_200_12_20-pid18910.params"

         elif dat["lcode"] == "uk" and dat["tcode"] == "iu":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Ukrainian/uk.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/uk.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/uk.vectors --pretrained_dim 100 "

            modelFile = "uk_iu_embed_parser_pos_2_200_100_20_200_12_20-pid17240.params" #"uk_ui_parser_pos_2_200_100_20_200_12_20-pid7910.params"

         elif dat["lcode"] == "ur" and dat["tcode"] == "udtb":
            parserCode = "parser/lstm-parse"
            dimension = 200
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Urdu/ur.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/ur.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/ur.vectors --pretrained_dim 100 "
            modelFile = "urdu_udtb_embed_parser_pos_2_200_100_20_200_12_20-pid11091.params" #"ur_udtb_parser_pos_2_200_100_20_200_12_20-pid21336.params"

         elif dat["lcode"] == "vi" and dat["tcode"] == "vtb":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/Vietnamese/vi.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/vi.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/vi.vectors --pretrained_dim 100 "
            modelFile = "vi_vtb_embed_parser_pos_2_100_100_20_100_12_20-pid3440.params" #"vi_vtb_parser_pos_2_100_100_20_100_12_20-pid31306.params"

         elif dat["lcode"] == "zh" and dat["tcode"] == "gsd":
            parserCode = "parser-bl/lstm-parse-bl"
            dimension = 100
            os.system("cp /media/training-datasets/universal-dependency-learning/conll17-ud-word-embeddings/ChineseT/zh.vectors.xz /mnt/data/embedding-files/")           
            os.system("unxz /mnt/data/embedding-files/zh.vectors.xz")
            embeddingCode = "-w /mnt/data/embedding-files/zh.vectors --pretrained_dim 100 "
            modelFile = "zh_gsd_embed_parser_pos_2_100_100_20_100_12_20-pid10893.params" #"zh_gsd_parser_pos_2_100_100_20_100_12_20-pid31672.params"

         else:
            parserCode = "parser/lstm-parse"
            dimension = 200
            lcode = "mix"
            tcode = "lang"
            embeddingCode = ""
            modelFile = "mix_lang_parser_pos_2_200_100_20_200_12_20-pid24428.params"


         traConlluFile = ""
         if lcode == "mix" and tcode == "lang":
            traConlluFile = "/media/data/mix_lang-ud-train.conllu"
         else:
            traConlluFile = trapath+"/"+lcode+"_"+tcode + ".conllu"
         traOracleFileName = "TrainingOracle_"+lcode+"-"+tcode+".txt"
         testOracleFileName = "TestOracle_"+lcode+"-"+tcode+".txt"



         print(traConlluFile)
         print(trapath+"/"+traConlluFile)
         print(devpath+"/"+dat["psegmorfile"])
     # print("model-files/"+modelName)

         os.system("java -jar MyParserOracleArcStdWithSwap.jar -t -1 -l 1 -c Temp/"+conllVersion+" > Temp/"+testOracleFileName)

         os.system(parserCode+" --cnn-mem 9000 -T /media/data/traOracles/"+traOracleFileName+" -d Temp/"+testOracleFileName+" --hidden_dim 100 --lstm_input_dim "+str(dimension)+"  "+embeddingCode+" --rel_dim 20 --action_dim 20 --input_dim "+str(dimension)+" -P -S --train_conll "+traConlluFile+" --dev_conll "+devpath+"/"+dat["psegmorfile"]+" --test_conll "+devpath+"/"+dat["psegmorfile"]+" -m  /media/data/"+modelFile+" > Temp/"+outputConll)

         os.system("perl postprocessing/restore_conllu_lines.pl Temp/"+outputConll+" "+devpath+"/"+dat["psegmorfile"]+" > "+outputdir+"/"+outputConllu)

         os.system("rm Temp/*.*")
         os.system("rm /mnt/data/embedding-files/*.*")

         parserCode = ""
         embeddingCode = ""
         modelFile = ""


if __name__ == "__main__":
   main(sys.argv[1:])
