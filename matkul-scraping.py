from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-profile")
# change your own profile
options.add_argument("C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/4trbl1o3.automation")
driver = webdriver.Firefox(options)
driver.maximize_window()

def ajaran_tahun_semester():

      tahun_ajaran = int(input(
      """
      Tahun Ajaran
      1. 2021
      2. 2022
      3. 2023
      ------------
      Pilih: """
      ))

      pilih_semester = int(input(
      """
      Semester
      1. Semester 1
      2. Semester 2
      --------------
      Pilih: """
      ))

      if tahun_ajaran == 1:
            if pilih_semester == 1:
                  tahun = "2021"
                  semester = "1"
            elif pilih_semester == 2:
                  tahun = "2021"
                  semester = "2"
            else:
                  print("Semester is not available")
      elif tahun_ajaran == 2:
            if pilih_semester == 1:
                  tahun = "2022"
                  semester = "1"
            elif pilih_semester == 2:
                  tahun = "2022"
                  semester = "2"
            else:
                  print("Semester is not available!")
      elif tahun_ajaran == 3:
            if pilih_semester == 1:
                  tahun = "2023"
                  semester = "1"
            elif pilih_semester == 2:
                  tahun = "2023"
                  semester = "2"
            else:
                  print("Semester is not available!")
      else:
            print("Tahun ajaran is not available!")
      
      return tahun, semester

def list_ajaran(year,semester):

      matkul_set = set()

      for page in range(0, 19): #total pages
            driver.get(f"https://eknows.uinsgd.ac.id/course/index.php?categoryid=6&page={str(page)}")
            print(f"Halaman: {page+1}")
            matkuls = driver.find_elements(By.PARTIAL_LINK_TEXT, year+semester)
            sleep(1.5)
            for matkul in matkuls:
                  if (matkul.text, matkul.get_attribute("href")) not in matkul_set:
                        matkul_set.add((matkul.text, matkul.get_attribute("href")))
                        
      for matkul in matkul_set:
            print(matkul[0], matkul[1])
      
      print(f"Total Mata kuliah : {len(matkul_set)}")

tahun, semester = ajaran_tahun_semester()
list_ajaran(tahun, semester)

driver.quit()
