import tkinter as tk
from tkinter import messagebox
import random
import os
import pygame

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Path to the folder containing bird sound files
SOUND_FOLDER = 'bird-songs'  # Update this path to your sound files

# Bird data structure
class Bird:
    def __init__(self, common_name, scientific_name, sound_file, quiz_num):
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.sound_file = sound_file
        self.quiz = quiz_num

# Bird data organized in order by quiz
bird_data = [
    # Quiz 1
    Bird('Greater White-Fronted Goose', 'Anser albifrons', 'GWFG.mp3', 1),
    Bird('Mallard', 'Anas platyrhyncos', 'MALL.mp3', 1),
    Bird('Northern Bobwhite', 'Colinus virginianus', 'NOBO.mp3', 1),
    Bird('Dusky Grouse', 'Dendragapus obscurus', 'DUGR.mp3', 1),
    Bird('Mourning Dove', 'Zenaida macroura', 'MODO.mp3', 1),
    Bird('Yellow-billed Cuckoo', 'Coccyzus americanus', 'YBCU.mp3', 1),
    Bird('Common Nighthawk', 'Chordeiles minor', 'CONI.mp3', 1),
    Bird('Chimney Swift', 'Chaetura pelagica', 'CHSW.mp3', 1),
    Bird('Broad-tailed Hummingbird', 'Selasphorus platycercus', 'BTHU.mp3', 1),

    #quiz 2
    Bird('Virginia Rail', 'Rallus limicola', 'VIRA.mp3', 2),
    Bird('Sandhill Crane', 'Grus canadensis', 'SACR.mp3', 2),
    Bird('Killdeer', 'Charadrius vociferus', 'KILL.mp3', 2),
    Bird('Upland Sandpiper', 'Bartramia longicauda', 'UPSA.mp3', 2),

    #quiz 3
    Bird('Common Loon', 'Gavia immer', 'COLO.mp3', 3),
    Bird('American Bittern', 'Botaurus lentiginosus', 'AMBI.mp3', 3),
    Bird('Bald Eagle', 'Haliaeetus leucocephalus', 'BAEA.mp3', 3),
    Bird('Red-tailed Hawk', 'Buteo jamaicensis', 'RTHA.mp3', 3),
    Bird('Barn Owl', 'Tyto alba', 'BAOW.mp3', 3),
    Bird('Eastern Screech-Owl', 'Megascops asio', 'ESOW.mp3', 3),
    Bird('Great Horned Owl', 'Bubo virginianus', 'GHOW.mp3', 3),
    Bird('Belted Kingfisher', 'Megaceryle alcyon', 'BEKI.mp3', 3),
    Bird('Downy Woodpecker', 'Dryobates pubescens', 'DOWO.mp3', 3),
    Bird('American Kestrel', 'Falco sparverius', 'AMKE.mp3', 3),

    #quiz 4
    Bird('Western Wood-Pewee', 'Contopus sodidulus', 'WWPE.mp3', 4),
    Bird('Least Flycatcher', 'Empidonax minimus', 'LEFL.mp3', 4),
    # Bird('Western Flycatcher', 'Empidonax difficilis', 'WEFL.mp3', 4), no recording on the slides, need to find one
    Bird('Western Kingbird', 'Tyrannus verticalis', 'WEKI.mp3', 4),
    Bird('Eastern Kingbird', 'Tyrannus tyrannus', 'EAKI.mp3', 4),
    Bird('Plumbeous Vireo', 'Vireo plumbeus', 'PLVI.mp3', 4),
    Bird('Warbling Vireo', 'Vireo gilvus', 'WAVI.mp3', 4),
    Bird('Blue Jay', 'Cyanocitta cristata', 'BLJA.mp3', 4),
    Bird('Black-billed Magpie', 'Pica hudsonia', 'BBMA.mp3', 4),
    Bird('Common Raven', 'Corvus corax', 'CORA.mp3', 4),
    Bird('Black-capped Chickadee', 'Poecile atricapillus', 'BCCH.mp3', 4),


    #quiz 5
    Bird('Cliff Swallow', 'Petrochelidon pyrrhonota', 'CLSW.mp3', 5),
    Bird('Bushtit', 'Psalitriparus minimus', 'BUSH.mp3', 5),
    Bird('White-breasted Nuthatch', 'Sitta carolinensis', 'WBNU.mp3', 5),
    Bird('House Wren', 'Troglodytes aedon', 'HOWR.mp3', 5),
    Bird('Townsend’s Solitaire', 'Myadestes townsendi', 'TOSO.mp3', 5),
    Bird('American Robin', 'Turdus migratorius', 'AMRO.mp3', 5),

    #quiz 6
    Bird('Evening Grosbeak', 'Coccothraustes vespertinus', 'EVGR.mp3', 6),
    Bird('Pine Siskin', 'Spinus pinus', 'PISI.mp3', 6),
    Bird('Chestnut-collared Longspur', 'Calcarius orantus', 'CCLO.mp3', 6),
    Bird('Lark Sparrow', 'Chondestes grammacus', 'LASP.mp3', 6),
    Bird('Lark Bunting', 'Calamospiza melanocorys', 'LABU.mp3', 6),
    Bird('Dark-eyed Junco', 'Junco hyemalis', 'DEJU.mp3', 6),
    Bird('White-crowned Sparrow', 'Zonotrichia leucophrys', 'WCSP.mp3', 6),
    Bird('Song Sparrow', 'Melospiza melodia', 'SOSP.mp3', 6),

    #quiz 7
    Bird('Yellow-breasted Chat', 'Icteria virens', 'YBCH.mp3', 7),
    Bird('Yellow-headed Blackbird', 'Xanthocephalus xanthocephalus', 'YHBL.mp3', 7),
    Bird('Bobolink', 'Dolichonyx oryzivorus', 'BOBO.mp3', 7),
    Bird('Red-winged Blackbird', 'Agelaius pheoniceus', 'RWBL.mp3', 7),
    Bird('MacGillivray’s Warbler', 'Geothlypis tolmiei', 'MAWA.mp3', 7),
    Bird('Common Yellowthroat', 'Geothlypis trichas', 'COYE.mp3', 7),
    Bird('Yellow Warbler', 'Setophaga petechia', 'YEWA.mp3', 7),
    Bird('Yellow-rumped Warbler', 'Setophaga coronata', 'YRWA.mp3', 7),
    Bird('Black-headed Grosbeak', 'Pheuticus melanocephalus', 'BHGR.mp3', 7),
    Bird('Lazuli Bunting', 'Passerina amoena', 'LAZBU.mp3', 7)
]

current_bird = None
quiz_mode = None
score_common = 0
score_scientific = 0
question_count = 0
selected_quiz = 1

# Function to start the quiz based on selection
def start_quiz(mode, quiz_num=None):
    global quiz_mode, score_common, score_scientific, question_count, selected_quiz
    quiz_mode = mode
    score_common = 0
    score_scientific = 0
    question_count = 0
    selected_quiz = quiz_num if quiz_num else 1
    start_page.pack_forget()
    quiz_page.pack()
    play_sound()
    update_question_info()

# Function to play a bird sound
def play_sound(replay=False):
    global current_bird
    if not replay:  # Only change the bird if not a replay
        if quiz_mode == 'all_birds':
            current_bird = random.choice([b for b in bird_data if b.quiz == selected_quiz])
        elif quiz_mode == 'random_10':
            current_bird = random.choice(bird_data)
    sound_path = os.path.join(SOUND_FOLDER, current_bird.sound_file)
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

# Function to check the user's answer
def check_answer():
    global score_common, score_scientific, question_count
    common_guess = common_name_entry.get().strip()
    scientific_guess = scientific_name_entry.get().strip()
    correct_common = current_bird.common_name
    correct_scientific = current_bird.scientific_name

    result_text = ''
    if common_guess == correct_common:
        score_common += 1
        result_text += f'Common Name: Correct! ({correct_common})\n'
    else:
        result_text += f'Common Name: Incorrect! The answer was: {correct_common}\n'

    if scientific_guess == correct_scientific:
        score_scientific += 1
        result_text += f'Scientific Name: Correct! ({correct_scientific})'
    elif scientific_guess == "":
        result_text += f'Scientific Name: {correct_scientific}'
    elif scientific_guess:
        result_text += f'Scientific Name: Incorrect! The answer was: {correct_scientific}'

    result_label.config(text=result_text)
    common_name_entry.delete(0, tk.END)
    scientific_name_entry.delete(0, tk.END)

    question_count += 1
    if (quiz_mode == 'all_birds' and question_count >= len([b for b in bird_data if b.quiz == selected_quiz])) or (quiz_mode == 'random_10' and question_count >= 10):
        show_score()
    else:
        play_sound()
        update_question_info()

# Function to show the score
def show_score():
    score_percentage_common = (score_common / question_count) * 100
    score_percentage_scientific = (score_scientific / question_count) * 100
    messagebox.showinfo('Quiz Complete', f'Common Name Score: {score_common} out of {question_count} ({score_percentage_common:.2f}%)\n'
                                    f'Scientific Name Score: {score_scientific} out of {question_count} ({score_percentage_scientific:.2f}%)')
    quiz_page.pack_forget()
    start_page.pack()

# Function to update question number display
def update_question_info():
    question_info_label.config(text=f'Question {question_count + 1}')

# GUI setup
app = tk.Tk()
app.title('Bird Sound Identification Game')
app.geometry('500x500')
app.config(bg='#f0f0f0')

# Start Page
start_page = tk.Frame(app, bg='#f0f0f0')
start_label = tk.Label(start_page, text='Bird Sound ID Game', font=('Helvetica', 20, 'bold'), bg='#f0f0f0')
start_label.pack(pady=20)

start_button_all = tk.Button(start_page, text='Random 10-Question Quiz', command=lambda: start_quiz('random_10'), font=('Helvetica', 14), bg='#4CAF50', fg='white')
start_button_all.pack(pady=10)

for i in range(1, 8):
    tk.Button(start_page, text=f'Quiz {i} - All Birds', command=lambda i=i: start_quiz('all_birds', i), font=('Helvetica', 14), bg='#4CAF50', fg='white').pack(pady=5)

start_page.pack()

# Quiz Page
quiz_page = tk.Frame(app, bg='#f0f0f0')
question_info_label = tk.Label(quiz_page, text='', font=('Helvetica', 14), bg='#f0f0f0')
question_info_label.pack(pady=5)

common_label = tk.Label(quiz_page, text='Common Name:', font=('Helvetica', 14), bg='#f0f0f0')
common_label.pack(pady=5)
common_name_entry = tk.Entry(quiz_page, font=('Helvetica', 14))
common_name_entry.pack(pady=5)

scientific_label = tk.Label(quiz_page, text='Scientific Name (Optional):', font=('Helvetica', 14), bg='#f0f0f0')
scientific_label.pack(pady=5)
scientific_name_entry = tk.Entry(quiz_page, font=('Helvetica', 14))
scientific_name_entry.pack(pady=5)

submit_button = tk.Button(quiz_page, text='Submit Guess', command=check_answer, font=('Helvetica', 14), bg='#4CAF50', fg='white')
submit_button.pack(pady=10)

result_label = tk.Label(quiz_page, text='', font=('Helvetica', 12), bg='#f0f0f0')
result_label.pack(pady=10)

replay_button = tk.Button(quiz_page, text='Replay Sound', command=lambda: play_sound(replay=True), font=('Helvetica', 14), bg='#2196F3', fg='white')
replay_button.pack(pady=5)

app.mainloop()