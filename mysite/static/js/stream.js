const APP_ID = 'b2ac44c57a4444c6ab4bd87f21aa60d7'
const CHANNEL = sessionStorage.getItem('room')
const TOKEN = sessionStorage.getItem('token')
let UID=Number(sessionStorage.getItem('UID'))
let NAME = sessionStorage.getItem('name')

const client = AgoraRTC.createClient({ mode: 'live', codec: 'vp8' });

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    try {
        document.getElementById('room-name').innerText=CHANNEL
        client.on('user-published', handleUserJoined);
        client.on('user-left', handleUserLeft);

        client.setClientRole('host');
        
        try{
            UID=await client.join(APP_ID, CHANNEL, TOKEN, UID);
        }catch(error){
            console.error("Failed to join the channel:", error);
            // Handle the error appropriately
        }
        localTracks = await AgoraRTC.createMicrophoneAndCameraTracks();
        let member =createMember()
        console.log('member:',member)

        let player = `<div class="video-container" id="user-container-${UID}">
           <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
            <div class="video-player" id="user-${UID}"></div>
           </div>`;
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);

        localTracks[1].play(`user-${UID}`);

        await client.publish([localTracks[0], localTracks[1]]);
    } catch (error) {
        console.error("Failed to join the channel and display local stream:", error);
        // Handle the error appropriately
    }
};


let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user;
    await client.subscribe(user, mediaType)

    if (mediaType === 'video') {
        let player = document.getElementById(`user-container-${user.uid}`)
        if (player != null) {
            player.remove()
        }
        player = `<div class="video-container" id="user-container-${user.uid}">
       <div class="username-wrapper"><span class="user-name">My Name</span></div>
        <div class="video-player" id="user-${user.uid}"></div>
       </div>`
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);
        user.videoTrack.play(`user-${user.uid}`)
    }
    if(mediaType== 'audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft = async(user)=>{
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}

let leaveAndRemoveLocalStream = async()=>{
    for(let i =0; localTracks.length>i;i++){
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()
    window.open('/videocall/','_self')
}

let toggleCamera = async () => {
    let cameraBtn = document.getElementById('camera-btn');
    if (localTracks[1].muted) {
        await localTracks[1].setMuted(false);
        cameraBtn.style.backgroundColor = '#fff';
    } else {
        await localTracks[1].setMuted(true);
        cameraBtn.style.backgroundColor = 'rgb(255,80,80,1)';
    }
};

let toggleMic = async () => {
    let micBtn = document.getElementById('mic-btn');
    if (localTracks[0].muted) {
        await localTracks[0].setMuted(false);
        micBtn.style.backgroundColor = '#fff';
    } else {
        await localTracks[0].setMuted(true);
        micBtn.style.backgroundColor = 'rgb(255,80,80,1)';
    }
};

let createMember = async()=>{
    let response = await fetch('/videocall/create_member/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({
            'UID':UID,
            'name':NAME,
            'room':CHANNEL
        })
    })

    let member = await response.json()
    return member
}

joinAndDisplayLocalStream();

document.getElementById('leave-btn').addEventListener('click',leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click',toggleCamera)
document.getElementById('mic-btn').addEventListener('click',toggleMic)