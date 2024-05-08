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
    let faults = 0;
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
    let pageLastUsed = {}; 
    let output = "<h2>Least Recently Used Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hits/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            hits++;
            result = 'H';
            pageLastUsed[reference] = i;
        } else {
            faults++;
            result = 'F';
            if (frames.length < frameSize) {
                frames.push(reference);
                pageLastUsed[reference] = i;
            } 
            else {
                let lruPage = frames.reduce((a, b) => pageLastUsed[a] < pageLastUsed[b] ? a : b);
                frames[frames.indexOf(lruPage)] = reference;
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
    const frequencyMap = {}; 
    const lastUsedMap = {}; 
    let output = "<h2>Least Frequently Used Page Replacement</h2><table><tr><th>Reference</th><th>Frames</th><th>Page Hits/Faults</th></tr>";

    for (let i = 0; i < references.length; i++) {
        const reference = references[i];
        if (frames.includes(reference)) {
            hits++;
            result = 'H';
            frequencyMap[reference]++;
            lastUsedMap[reference] = i; 
        } else {
            faults++;
            result = 'F';
            if (frames.length < frameSize) {
                frames.push(reference);
                frequencyMap[reference] = 1;
                lastUsedMap[reference] = i;
            } else {
                let leastFrequentPage = frames[0];
                for (let j = 1; j < frames.length; j++) {
                    if (frequencyMap[frames[j]] < frequencyMap[leastFrequentPage]) {
                        leastFrequentPage = frames[j];
                    } 
                    else if (frequencyMap[frames[j]] === frequencyMap[leastFrequentPage]) {
                        if (lastUsedMap[frames[j]] < lastUsedMap[leastFrequentPage]) {
                            leastFrequentPage = frames[j];
                        }
                    }
                }
                frames[frames.indexOf(leastFrequentPage)] = reference;
                frequencyMap[reference] = 1;
                delete frequencyMap[leastFrequentPage];
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
                let index = findOptimalIndex(references, frames, i); 
                frames[index] = reference; 
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

function findOptimalIndex(references, frames, currentIndex) { 
    let optimalIndex = -1;
    let farthestDistance = -1; 
    for (let i = 0; i < frames.length; i++) { 
        let index = currentIndex + 1; 
        while (index < references.length) {
            if (references[index] === frames[i]) {
                if (index > farthestDistance) {
                    farthestDistance = index;
                    optimalIndex = i;
                }
                break;
            }
            index++;
        }
        if (index === references.length) {
            return i;
        }
    }
    return optimalIndex;
}
