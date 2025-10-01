#!/usr/bin/env python3
import subprocess, sys
def run(cmd):
    print("\n========== RUNNING:", ' '.join(cmd))
    sys.stdout.flush()
    subprocess.run(cmd, check=True)
run(["python3","scripts/task1_load_dataset.py"])
run(["python3","scripts/task2_tokenize.py"])
run(["python3","scripts/task3_word_freq.py"])
print("\n✅ All tasks completed.")
