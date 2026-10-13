import gzip
import shutil

def gzip_file(src, dst):
    with open(src, "rb") as f_in:
        with gzip.open(dst, "wb", compresslevel=9) as f_out:
            shutil.copyfileobj(f_in, f_out)
    import os
    size_mb = os.path.getsize(dst) / 1024 / 1024
    print(f"  {src} -> {dst} ({size_mb:.2f} MB)")
    
gzip_file("jie_boss_pi.json", "jie_boss_pi.json.gz")
gzip_file("jie_2v3_pi.json", "jie_2v3_pi.json.gz")