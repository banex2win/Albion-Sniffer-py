import subprocess
import threading
import json
import re


#["Id", "UnitPriceSilver", "TotalPriceSilver", "Amount", "Tier", "IsFinished",
# "AuctionType", "HasBuyerFetched", "HasSellerFetched", "SellerCharacterId",
# "SellerName", "BuyerCharacterId", "BuyerName", "ItemTypeId", "ItemGroupTypeId",
# "EnchantmentLevel", "QualityLevel", "Expires", "ReferenceId"]

class Sniffer:
    def __init__(self):
        self.process = None
        self.output = ''
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        # Start the subprocess in a separate thread
        if not self.running:
            self.running = True
            self.output = ''  # Clear previous output
            self.process = subprocess.Popen(
                [
                    r"C:\Program Files\Albion Data Client\albiondata-client.exe",
                    "-debug",
                    "-events", "0",
                    "-operations", "75,76",
                    "-ignore-decode-errors"
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
            )

            # Start a thread to read the output
            self.read_thread = threading.Thread(target=self._read_output)
            self.read_thread.start()

    def _read_output(self):
        # Read the output from the process line by line
        while self.running:
            output_line = self.process.stdout.readline()
            if output_line:
                with self.lock:
                    self.output += output_line
            else:
                break
            
        self.process.stdout.close()
    
    def stop(self):
        if self.running:
            self.running = False
            self.process.terminate()  # Terminate the process
            self.process.wait()  # Wait for the process to terminate
            self.read_thread.join()  # Wait for the reading thread to finish
    
    def get_output(self):
        with self.lock:
            captured_output = self.output
            out = []
            # Perform the reconstruction steps
            captured_output = re.findall(r'(\[\{.*?\}\])', captured_output)
            captured_output = ''.join(captured_output)
            captured_output = captured_output.replace("][", ' ')
            captured_output = captured_output.replace("}", "},")

            captured_output = captured_output.replace("false", '"false"')
            captured_output = captured_output.replace("null", '"null"')
            captured_output = captured_output.replace("},]", "}]")

            try:
                out = json.loads(captured_output)
            except json.decoder.JSONDecodeError:
                print('No Avilable Items')
                pass


            for order in out:
                order["UnitPriceSilver"] /= 10000
                order["TotalPriceSilver"] /= 10000

            return out

