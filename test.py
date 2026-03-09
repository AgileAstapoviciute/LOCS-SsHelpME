"""
SECURITY CAMERA VULNERABILITY TESTING FRAMEWORK
"""

import socket
import requests
import time
from typing import Optional, Dict, List

class CameraSecurityAnalyzer:
    def __init__(self, camera_ip: str, test_id: str = "TEST_001"):
        """
        Initialize with target camera IP.
        
        Args:
            camera_ip: IP address of the camera in environment
            test_id: identifier for logging
        """
        self.camera_ip = camera_ip
        self.test_id = test_id
        self.results = {}
        
        # Common default credentials (test data) - add 
        self.default_credentials = [
            {'user': 'admin', 'pass': 'admin'},
            {'user': 'admin', 'pass': 'password'},
            {'user': 'admin', 'pass': '123456'},
            {'user': 'camera', 'pass': 'camera'},
            {'user': 'mirolentai@gmail.com', 'pass': 'agile123'},

        ]
    
    def test_default_credentials(self) -> Dict:
        """
        Test for default username/password combinations.
        Demonstrates why changing defaults is crucial.
        
        Returns:
            Dictionary with test results
        """
        print(f"[{self.test_id}] Testing default credentials on {self.camera_ip}")
        
        vulnerable_combinations = []
        
        # Hypothetical login endpoint - add possible endpoints
        login_endpoints = []
        
        for endpoint in login_endpoints:
            for creds in self.default_credentials:
                try:
                    # Simulate login attempt
                    # In real scenarios, the actual API would be analyzed first
                    response = requests.post(
                        endpoint,
                        data={'username': creds['user'], 'password': creds['pass']},
                        timeout=5
                    )
                    
                    # Check for successful login indicators
                    if response.status_code == 200 and "success" in response.text.lower():
                        vulnerable_combinations.append(creds)
                        print(f"  [!] DEFAULT CREDENTIALS WORK: {creds['user']}:{creds['pass']}")
                        
                except requests.RequestException as e:
                    # Endpoint not found or connection failed
                    continue
        
        self.results['default_creds'] = {
            'vulnerable': len(vulnerable_combinations) > 0,
            'found_credentials': vulnerable_combinations,
            'recommendation': 'Always change default credentials immediately'
        }
        
        return self.results['default_creds']
    
    def test_open_ports(self, ports: List[int] = [80, 443, 554, 8080, 23]) -> Dict:
        """
        Scan for open ports that shouldn't be exposed.
        
        Args:
            ports: List of ports to check (common IoT camera ports)
            
        Returns:
            Open ports found
        """
        print(f"[{self.test_id}] Scanning open ports on {self.camera_ip}")
        
        open_ports = []
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((self.camera_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"  [+] Port {port} is OPEN")
            
            sock.close()
            time.sleep(0.1)  # Avoid flooding
        
        self.results['open_ports'] = {
            'ports_found': open_ports,
            'risk_assessment': self._assess_port_risk(open_ports),
            'recommendation': 'Close unnecessary ports, use firewalls'
        }
        
        return self.results['open_ports']
    
    def test_unencrypted_streams(self) -> Dict:
        """
        Check for unencrypted video streams (RTSP, HTTP).
        """
        print(f"[{self.test_id}] Checking for unencrypted streams")
        
        # Common RTSP stream URLs (examples) - find out more
        rtsp_patterns = [
            f"rtsp://{self.camera_ip}:554/stream1",
            f"rtsp://{self.camera_ip}:8554/live",
            f"rtsp://{self.camera_ip}/live.sdp",
        ]
        
        unencrypted_streams = []
        
        for stream_url in rtsp_patterns:
            try:
                # Simple test to see if stream might be accessible
                # maybe use RTSP client libraries?
                test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_socket.settimeout(2)
                
                ip = self.camera_ip
                port = 554
                
                result = test_socket.connect_ex((ip, port))
                if result == 0:
                    unencrypted_streams.append(stream_url)
                    print(f"  [!] Potential unencrypted stream: {stream_url}")
                
                test_socket.close()
                
            except Exception as e:
                continue
        
        self.results['unencrypted_streams'] = {
            'found': unencrypted_streams,
            'risk': 'HIGH' if unencrypted_streams else 'LOW',
            'recommendation': 'Use encrypted protocols (RTSPS, HTTPS)'
        }
        
        return self.results['unencrypted_streams']
    
    def _assess_port_risk(self, ports: List[int]) -> str:
        high_risk_ports = [23, 21, 22, 3389]  # Telnet, FTP, SSH, RDP
        
        for port in ports:
            if port in high_risk_ports:
                return "HIGH - Critical services exposed"
        
        if 80 in ports or 554 in ports:
            return "MEDIUM - Unencrypted services"
        
        return "LOW - Only necessary services"
    
    def generate_report(self) -> str:
        """
        Generate report.
        """
        report = f"""
        SECURITY TEST REPORT - IOT CAMERA ANALYSIS
        Lab ID: {self.test_id}
        Device: XUMIUZIY Mini Security Camera
        Test Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
        Target IP: {self.camera_ip}
        
        SUMMARY OF FINDINGS:
        
        1. DEFAULT CREDENTIALS TEST:
           Vulnerable: {self.results.get('default_creds', {}).get('vulnerable', False)}
           Found Credentials: {self.results.get('default_creds', {}).get('found_credentials', [])}
           
        2. NETWORK EXPOSURE:
           Open Ports: {self.results.get('open_ports', {}).get('ports_found', [])}
           Risk Level: {self.results.get('open_ports', {}).get('risk_assessment', 'Not tested')}
           
        3. STREAM SECURITY:
           Unencrypted Streams Found: {len(self.results.get('unencrypted_streams', {}).get('found', []))}
        """
        return report

# IMPLEMENTATION

def run_test():
    print("CAMERA VULNERABILITY ANALYSIS")
    # IMPORTANT: IP must be of camera
    lab_camera_ip = ""  # CHANGE THIS to camera IP
    
    # Initialize analyzer
    analyzer = CameraSecurityAnalyzer(
        camera_ip=lab_camera_ip,
        test_id="LOCS_01"
    )
    
    # Run security tests
    print("\n[PHASE 1] Testing default credentials...")
    analyzer.test_default_credentials()
    
    print("\n[PHASE 2] Scanning for open ports...")
    analyzer.test_open_ports()
    
    print("\n[PHASE 3] Checking stream encryption...")
    analyzer.test_unencrypted_streams()
    
    # Generate report
    print("REPORT GENERATION")
    
    report = analyzer.generate_report()
    print(report)
    
    # Save report to file for lab submission
    with open(f"camera_security_report_{time.strftime('%Y%m%d')}.txt", "w") as f:
        f.write(report)
    
    print("\n[✓] Test completed. Report saved to file.")

# EXECUTION BLOCK 
if __name__ == "__main__":
    run_test()
