import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class info{
        int x, y , time;

        public info(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

    static char [][]map;
    static int w,h, answer;
    static boolean [][] visited;
    static Queue<info> fire;
    static Queue<info> person;
    static int [] dx = {-1,0,1,0};
    static int [] dy = {0,1,0,-1};


    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for(int tc=0;tc<T;tc++) {
            st = new StringTokenizer(br.readLine()," ");
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            map = new char[h][w];
            visited = new boolean[h][w];

            fire = new LinkedList<>();
            person = new LinkedList<>();

            for(int i=0;i<h;i++) {
                String str = br.readLine();
                for(int j=0;j<w;j++) {
                    map[i][j]= str.charAt(j);
                    if(map[i][j]=='@') person.offer(new info(i,j,0));
                    else if(map[i][j]=='*') fire.offer(new info(i,j,0));
                }
            }

            answer =0;
            bfs();
            if(answer==0) sb.append("IMPOSSIBLE\n");
            else sb.append(answer+"\n");
        }
        System.out.println(sb.toString());
    }

    public static void bfs() {


        while(!person.isEmpty()) {
            int size = fire.size();
            for(int i=0;i<size;i++) {
                info temp = fire.poll();
                for(int d=0;d<4;d++) {
                    int nx = temp.x+dx[d];
                    int ny = temp.y+dy[d];

                    if(range(nx,ny) && (map[nx][ny]=='.' || map[nx][ny]=='@')){
                        map[nx][ny]='*';
                        fire.offer(new info(nx,ny,0));
                    }
                }
            }

            size = person.size();
            for(int i=0;i<size;i++) {
                info temp = person.poll();
                for(int d=0;d<4;d++) {
                    int nx = temp.x+dx[d];
                    int ny = temp.y+dy[d];

                    if(!range(nx,ny)) {
                        answer = temp.time+1;
                        return;
                    }

                    if(map[nx][ny]=='.'){
                        map[nx][ny]='@';
                        person.offer(new info(nx,ny,temp.time+1));
                    }

                }
            }
        }
    }

    public static boolean range(int x, int y) {
        return x>=0 && y>=0 && x<h && y<w;
    }

}
