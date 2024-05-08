function simulate() {
    document.getElementById('output').innerHTML = '';
    const algo = document.getElementById('algo').value;
    if (algo == 'fifo') {
        simulatefifo();
    } else if (algo == 'lru') {
        simulatelru();
    } else if (algo == 'lfu') {
        simulatelfu();
    } else if (algo == 'opt') {
        simulateoptimal();
    } else {
        simulatefifo();
        simulatelru();
        simulatelfu();
        simulateoptimal();
    }
}


function simulatefifo() {
    const frameSize = document.getElementById('frameSize').value;
    const referenceString = document.getElementById('referenceString').value.trim();
    const references = referenceString.split(',').map(Number);
    
    let frames = [];
    let hits = 0;
    let faults = 0; //counter
    let result = '';
    let output = "<h2>First In First Out Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hit/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            result = 'H';
            hits++;
        } 
        else {
            result = 'F';
            faults++;
            if (frames.length < frameSize) {
                frames.push(reference);
            } 
            else {
                frames.shift();
                frames.push(reference);
            }
        }
        output += `<tr><td>${reference}</td><td>${frames.join(', ')}</td><td>${result}</td></tr>`;
    }

    var hratio = (hits/(references.length));
    var fratio = (faults/(references.length));

    output += `<tr><td colspan="2">Total Page Hits:</td><td>${hits}</td></tr>`;
    output += `<tr><td colspan="2">Total Page Faults:</td><td>${faults}</td></tr>`;
    output += `<tr><td colspan="2">Hit Ratio:</td><td>${hratio}</td></tr>`;
    output += `<tr><td colspan="2">Fault Ratio:</td><td>${fratio}</td></tr>`;
    output += "</table>";

    document.getElementById('output').innerHTML += output;
}

function simulatelru() {
    const frameSize = document.getElementById('frameSize').value;
    const referenceString = document.getElementById('referenceString').value.trim();
    const references = referenceString.split(',').map(Number);
    
    let frames = [];
    let hits = 0;
    let faults = 0;
    let result = '';
    let pageLastUsed = {}; // Object to track the last usage of each page
    let output = "<h2>Least Recently Used Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hits/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            hits++;
            result = 'H';
            // Update the last usage of the page
            pageLastUsed[reference] = i;
        } else {
            faults++;
            result = 'F';
            if (frames.length < frameSize) {
                frames.push(reference);
                // Initialize last usage of the new page
                pageLastUsed[reference] = i;
            } 
            else {
                // Find the least recently used page in frames
                let lruPage = frames.reduce((a, b) => pageLastUsed[a] < pageLastUsed[b] ? a : b);
                // Replace the least recently used page with the new page
                frames[frames.indexOf(lruPage)] = reference;
                //frames[0] = reference
                // Update the last usage of the new page
                pageLastUsed[reference] = i;
            }
        }
        output += `<tr><td>${reference}</td><td>${frames.join(', ')}</td><td>${result}</td></tr>`;
    }
    var hratio = (hits/(references.length));
    var fratio = (faults/(references.length));

    output += `<tr><td colspan="2">Total Page Hits:</td><td>${hits}</td></tr>`;
    output += `<tr><td colspan="2">Total Page Faults:</td><td>${faults}</td></tr>`;
    output += `<tr><td colspan="2">Hit Ratio:</td><td>${hratio}</td></tr>`;
    output += `<tr><td colspan="2">Fault Ratio:</td><td>${fratio}</td></tr>`;
    output += "</table>";
    document.getElementById('output').innerHTML += output;
}

function simulatelfu() {
    const frameSize = document.getElementById('frameSize').value;
    const referenceString = document.getElementById('referenceString').value.trim();
    const references = referenceString.split(',').map(Number);
    
    let frames = [];
    let hits = 0;
    let faults = 0;
    let result = '';
    const frequencyMap = {}; // Map to track the frequency of each page
    const lastUsedMap = {}; // Map to track the last used index of each page
    let output = "<h2>Least Frequently Used Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hits/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            hits++;
            result = 'H';
            // Increment the frequency of the referenced page
            frequencyMap[reference]++;
            lastUsedMap[reference] = i; // Update the last used index
        } else {
            faults++;
            result = 'F';
            if (frames.length < frameSize) {
                frames.push(reference);
                // Initialize frequency of the new page
                frequencyMap[reference] = 1;
                lastUsedMap[reference] = i; // Update the last used index
            } else {
                // Find the page with the lowest frequency
                let leastFrequentPage = frames[0];
                for (let j = 1; j < frames.length; j++) {
                    if (frequencyMap[frames[j]] < frequencyMap[leastFrequentPage]) {
                        leastFrequentPage = frames[j];
                    } 
                    else if (frequencyMap[frames[j]] === frequencyMap[leastFrequentPage]) {
                        // If frequencies are equal, use LFU
                        if (lastUsedMap[frames[j]] < lastUsedMap[leastFrequentPage]) {
                            leastFrequentPage = frames[j];
                        }
                    }
                }
                // Replace the least frequent page with the new page
                frames[frames.indexOf(leastFrequentPage)] = reference;
                // Update frequency of the new page
                frequencyMap[reference] = 1;
                // Remove frequency count of the least frequent page
                delete frequencyMap[leastFrequentPage];
                // Update the last used index of the new page
                lastUsedMap[reference] = i;
            }
        }
        output += `<tr><td>${reference}</td><td>${frames.join(', ')}</td><td>${result}</td></tr>`;
    }

    var hratio = (hits/(references.length));
    var fratio = (faults/(references.length));

    output += `<tr><td colspan="2">Total Page Hits:</td><td>${hits}</td></tr>`;
    output += `<tr><td colspan="2">Total Page Faults:</td><td>${faults}</td></tr>`;
    output += `<tr><td colspan="2">Hit Ratio:</td><td>${hratio}</td></tr>`;
    output += `<tr><td colspan="2">Fault Ratio:</td><td>${fratio}</td></tr>`;
    output += "</table>";
    document.getElementById('output').innerHTML += output;
}

function simulateoptimal() {
    const frameSize = document.getElementById('frameSize').value;
    const referenceString = document.getElementById('referenceString').value.trim();
    const references = referenceString.split(',').map(Number);
    
    let frames = [];
    let hits = 0;
    let faults = 0;
    let result = '';
    let output = "<h2>Optimal Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hits/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            hits++;
            result = 'H';
        } else {
            faults++;
            result = 'F';
            if (frames.length < frameSize) {
                frames.push(reference);
            } else {
                // Find the index of the page in frames that won't be used for the longest period in the future
                let index = findOptimalIndex(references, frames, i); //0
                frames[index] = reference; // Replace the page at that index with the current reference
            }
        }
        output += `<tr><td>${reference}</td><td>${frames.join(', ')}</td><td>${result}</td></tr>`;
    }
    var hratio = (hits/(references.length));
    var fratio = (faults/(references.length));

    output += `<tr><td colspan="2">Total Page Hits:</td><td>${hits}</td></tr>`;
    output += `<tr><td colspan="2">Total Page Faults:</td><td>${faults}</td></tr>`;
    output += `<tr><td colspan="2">Hit Ratio:</td><td>${hratio}</td></tr>`;
    output += `<tr><td colspan="2">Fault Ratio:</td><td>${fratio}</td></tr>`;
    output += "</table>";
    document.getElementById('output').innerHTML += output;
}

function findOptimalIndex(references, frames, currentIndex) { // 7 0 1 2 0 3 4 2 3 0 3 2 1 2 0 1 7 0 1  // frames = [7 0 1]
    let optimalIndex = -1; //0
    let farthestDistance = -1; //17
    for (let i = 0; i < frames.length; i++) { //irr frames
        let index = currentIndex + 1; // say index = 3 + 1 = 4
        while (index < references.length) { //right after page to end of ref string: 4-20
            if (references[index] === frames[i]) { //ref[4] = 0; 
                if (index > farthestDistance) {
                    farthestDistance = index;
                    optimalIndex = i;
                }
                break;
            }
            index++;
        }
        // If the page is not found in future references, it is the best candidate for replacement
        if (index === references.length) {
            return i;
        }
    }
    return optimalIndex;
}
